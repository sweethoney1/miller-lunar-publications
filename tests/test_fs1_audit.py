"""Software checks using fabricated audit rows, not simulated market evidence."""
import csv
import importlib.util
import io
from pathlib import Path
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / "skills/market-state-measurement-first/scripts/read_fs1_audit.py"
SPEC = importlib.util.spec_from_file_location("fs1_reader", SCRIPT)
reader = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(reader)


def fixture(equal_cuts=False):
    from datetime import date, timedelta
    rows = []
    values = [2, .25, 50, 25] if equal_cuts else [1, .2, 55, 20]
    for i in range(41):
        row = dict.fromkeys(reader.HEADERS, "")
        row.update(server_day=(date(2020, 1, 1) + timedelta(days=i)).strftime("%Y.%m.%d"),
                   minutes="1000", data_verified="true", data_mode="UNIVERSAL",
                   bo_events="1", bo_success="0", mr_events="2", mr_success="1",
                   fingerprint="NA" if i < 20 else ("FS1-F00" if equal_cuts else "FS1-F02"))
        for a, p, v, c in zip(reader.AXES, reader.PREFIX, values, [2, .25, 50, 25]):
            row[p + "_fixed_cut"] = str(c)
            if i >= 20:
                row[a] = str(v)
            if i >= 40:
                row[p + "_lag20"] = str(v)
                row[p + "_delta20"] = "0"
        rows.append(row)
    return rows


def parse(rows, encoding="utf-8-sig"):
    s = io.StringIO()
    w = csv.DictWriter(s, reader.HEADERS)
    w.writeheader()
    w.writerows(rows)
    with tempfile.TemporaryDirectory() as directory:
        p = Path(directory) / "fixture.csv"
        p.write_bytes(s.getvalue().encode(encoding))
        return reader.read_rows(p)[0]


class AuditReaderTests(unittest.TestCase):
    def test_na_rows_and_missing_pulse_remain_visible(self):
        for encoding in ["utf-8-sig", "utf-16"]:
            with self.subTest(encoding=encoding):
                out = reader.inspect_rows(parse(fixture(), encoding))
                self.assertEqual(out["status"], "EXPORT_CHECKS_PASSED")
                self.assertEqual(out["fingerprint_NA_rows"], 20)
                self.assertEqual(out["pulse_available_rows"], 0)
                self.assertEqual(out["latest_observed_row"]["server_day"], "2020.02.10")

    def test_equality_uses_lower_bit(self):
        out = reader.inspect_rows(parse(fixture(equal_cuts=True)))
        self.assertEqual(out["status"], "EXPORT_CHECKS_PASSED")
        self.assertEqual(out["code_counts"]["FS1-F00"], 21)

    def test_corrupted_label_and_delta_are_reported(self):
        rows = fixture()
        rows[-1]["fingerprint"] = "FS1-F15"
        rows[-1]["vol_delta20"] = "7"
        out = reader.inspect_rows(parse(rows))
        self.assertEqual(out["error_count"], 2)
        self.assertEqual(out["status"], "EXPORT_INCONSISTENT")
        rows = fixture()
        rows[-1]["vol_fixed_cut"] = "3"
        self.assertEqual(reader.inspect_rows(parse(rows))["error_count"], 1)

    def test_mixed_pipeline_is_rejected(self):
        rows = fixture()
        rows[-1]["data_mode"] = "LEGACY_XAU"
        with self.assertRaisesRegex(ValueError, "data_mode"):
            reader.inspect_rows(parse(rows))

    def test_duplicate_date_and_nonfinite_values_are_rejected(self):
        rows = fixture()
        rows[-1]["server_day"] = rows[-2]["server_day"]
        with self.assertRaisesRegex(ValueError, "strictly increasing"):
            parse(rows)
        rows = fixture()
        rows[-1]["volatility"] = "nan"
        with self.assertRaisesRegex(ValueError, "Nonfinite"):
            parse(rows)

    def test_unverified_latest_row_is_not_replaced(self):
        rows = fixture()
        rows[-1]["data_verified"] = "false"
        out = reader.inspect_rows(parse(rows))
        self.assertGreater(out["error_count"], 0)
        self.assertFalse(out["latest_observed_row"]["data_verified"])
        self.assertEqual(out["latest_observed_row"]["server_day"], "2020.02.10")


if __name__ == "__main__":
    unittest.main()
