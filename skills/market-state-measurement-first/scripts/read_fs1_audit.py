#!/usr/bin/env python3
"""Read and cross-check FS1 v0.31 audit exports; do not calculate market axes."""
import argparse
import csv
import hashlib
import io
import json
import math
from collections import Counter
from datetime import datetime, timedelta
from pathlib import Path

AXES = ("volatility", "trend", "breakout", "meanrev")
PREFIX = ("vol", "trend", "breakout", "meanrev")
HEADERS = (
    "server_day", "minutes", "data_verified", "data_mode", "bo_events", "bo_success",
    "mr_events", "mr_success", *AXES,
    *(p + "_lag20" for p in PREFIX), *(p + "_delta20" for p in PREFIX),
    *(p + "_scale252" for p in PREFIX), *(p + "_z" for p in PREFIX),
    "D", "pulse", "fingerprint", *(p + "_fixed_cut" for p in PREFIX),
)
NUMERIC = set(HEADERS) - {"server_day", "data_verified", "data_mode", "fingerprint"}
COUNTS = ("minutes", "bo_events", "bo_success", "mr_events", "mr_success")


def read_rows(path):
    raw = Path(path).read_bytes()
    encoding = "utf-16" if raw[:2] in (b"\xff\xfe", b"\xfe\xff") else "utf-8-sig"
    text = raw.decode(encoding)
    reader = csv.DictReader(io.StringIO(text))
    if reader.fieldnames is None or len(reader.fieldnames) != len(set(reader.fieldnames)):
        raise ValueError("Missing or duplicate CSV header")
    missing = sorted(set(HEADERS) - set(reader.fieldnames))
    if missing:
        raise ValueError("Missing FS1 v0.31 fields: " + ", ".join(missing))
    rows = []
    for line, row in enumerate(reader, 2):
        if None in row or any(row[k] is None for k in HEADERS):
            raise ValueError(f"Malformed CSV row at line {line}")
        row = {k: v.strip() for k, v in row.items()}
        day = datetime.strptime(row["server_day"], "%Y.%m.%d")
        if rows and day <= rows[-1]["_day"]:
            raise ValueError(f"Dates not strictly increasing at line {line}")
        row["_day"] = day
        flag = row["data_verified"].lower()
        if flag not in ("true", "false", "1", "0"):
            raise ValueError(f"Invalid data_verified at line {line}")
        row["data_verified"] = flag in ("true", "1")
        for key in NUMERIC:
            value = row[key]
            if value in ("", "NA"):
                row[key] = None
                continue
            row[key] = float(value)
            if not math.isfinite(row[key]):
                raise ValueError(f"Nonfinite {key} at line {line}")
        for key in COUNTS:
            value = row[key]
            if value is None or value < 0 or int(value) != value:
                raise ValueError(f"Invalid count {key} at line {line}")
            row[key] = int(value)
        for event in ("bo", "mr"):
            if row[event + "_success"] > row[event + "_events"]:
                raise ValueError(f"Success count exceeds events at line {line}")
        rows.append(row)
    if not rows:
        raise ValueError("Empty audit CSV")
    return rows, hashlib.sha256(raw).hexdigest()


def close(a, b):
    if a is None or b is None:
        return a is b
    return math.isclose(a, b, rel_tol=1e-9, abs_tol=1e-9)


def inspect_rows(rows, mode="UNIVERSAL"):
    if {r["data_mode"] for r in rows} != {mode}:
        raise ValueError("Mixed or unexpected data_mode; compare one declared pipeline per file")
    errors = []
    error_count = 0

    def issue(day, field, message):
        nonlocal error_count
        error_count += 1
        if len(errors) < 25:
            errors.append({"server_day": day, "field": field, "message": message})

    for i, row in enumerate(rows):
        day = row["server_day"]
        for axis, prefix in zip(AXES, PREFIX):
            expected_lag = rows[i - 20][axis] if i >= 20 else None
            if not close(row[prefix + "_lag20"], expected_lag):
                issue(day, prefix + "_lag20", "Not the exported value 20 row positions earlier")
            lag = row[prefix + "_lag20"]
            delta = row[axis] - lag if row[axis] is not None and lag is not None else None
            if not close(row[prefix + "_delta20"], delta):
                issue(day, prefix + "_delta20", "Does not equal current minus exported lag")
            if row[axis] is not None:
                upper = 1 if axis == "trend" else (100 if axis in ("breakout", "meanrev") else math.inf)
                if row[axis] < -1e-9 or row[axis] > upper + 1e-9:
                    issue(day, axis, "Outside the field's declared units")
            if row[prefix + "_fixed_cut"] is None:
                issue(day, prefix + "_fixed_cut", "Missing exported boundary")
            elif not close(row[prefix + "_fixed_cut"], rows[0][prefix + "_fixed_cut"]):
                issue(day, prefix + "_fixed_cut", "Fixed boundary changed within the file")
        cuts_ready = all(row[p + "_fixed_cut"] is not None for p in PREFIX)
        axes_ready = all(row[a] is not None for a in AXES)
        if not row["data_verified"] and any(row[a] is not None for a in AXES):
            issue(day, "data_verified", "Unverified observation has published State values")
        expected_code = "NA"
        if axes_ready and cuts_ready:
            code = 0
            for axis, prefix in zip(AXES, PREFIX):
                code = 2 * code + int(row[axis] > row[prefix + "_fixed_cut"])
            expected_code = f"FS1-F{code:02d}"
        if row["fingerprint"] != expected_code:
            issue(day, "fingerprint", "Does not match raw axes and exported cuts")
        if row["pulse"] is not None and not 0 <= row["pulse"] <= 100:
            issue(day, "pulse", "Outside 0 to 100")
        if row["D"] is not None and row["D"] < 0:
            issue(day, "D", "Negative change magnitude")

    latest = rows[-1]
    summary = {
        "status": "EXPORT_CHECKS_PASSED" if not error_count else "EXPORT_INCONSISTENT",
        "scope": "CSV schema, counts, lag/delta arithmetic, fingerprint encoding and value bounds; no raw-price replay or predictive test",
        "data_mode": mode,
        "rows": len(rows),
        "server_day_span": [rows[0]["server_day"], latest["server_day"]],
        "export_data_verified_rows": sum(r["data_verified"] for r in rows),
        "fingerprint_available_rows": sum(r["fingerprint"] != "NA" for r in rows),
        "fingerprint_NA_rows": sum(r["fingerprint"] == "NA" for r in rows),
        "pulse_available_rows": sum(r["pulse"] is not None for r in rows),
        "code_counts": dict(sorted(Counter(r["fingerprint"] for r in rows).items())),
        "axis_support": {
            a: {"available": sum(r[a] is not None for r in rows),
                "NA": sum(r[a] is None for r in rows),
                "min": min((r[a] for r in rows if r[a] is not None), default=None),
                "max": max((r[a] for r in rows if r[a] is not None), default=None)}
            for a in AXES
        },
        "latest_observed_row": {
            "server_day": latest["server_day"],
            "available_at_server_clock": (latest["_day"] + timedelta(days=1)).isoformat(sep=" "),
            "data_verified": latest["data_verified"],
            "fingerprint": latest["fingerprint"], "pulse": latest["pulse"],
            "exported_cuts": {a: latest[p + "_fixed_cut"] for a, p in zip(AXES, PREFIX)},
            "axes": {a: {"value": latest[a], "lag20": latest[p + "_lag20"],
                          "delta20": latest[p + "_delta20"]} for a, p in zip(AXES, PREFIX)},
        },
        "error_count": error_count, "first_errors": errors,
        "limits": [
            "data_verified is the exporter flag, not an independent feed audit",
            "Missing whole sessions require an external session calendar to detect",
            "The last observed row is reported even when values are missing or unverified",
            "No zero filling, missing-row deletion, trade gate or forecast is applied",
        ],
    }
    return summary


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv_file", type=Path)
    parser.add_argument("--mode", choices=("UNIVERSAL", "LEGACY_XAU"), default="UNIVERSAL")
    parser.add_argument("--output", type=Path, help="Optional JSON output path")
    args = parser.parse_args()
    if args.output and args.output.resolve() == args.csv_file.resolve():
        parser.error("Output path must differ from the input CSV")
    try:
        rows, sha = read_rows(args.csv_file)
        result = inspect_rows(rows, args.mode)
        result["input_sha256"] = sha
        result["input_filename"] = args.csv_file.name
    except (ValueError, OSError, UnicodeError) as exc:
        parser.exit(2, f"FS1 audit rejected: {exc}\n")
    output = json.dumps(result, indent=2, ensure_ascii=False, allow_nan=False) + "\n"
    if args.output:
        args.output.write_text(output, encoding="utf-8")
    else:
        print(output, end="")
    raise SystemExit(0 if result["error_count"] == 0 else 2)


if __name__ == "__main__":
    main()
