# FS1 UNIVERSAL Worked Measurement Example

**Documentation edition v1.1 | 2026-10-22**

Use FS1 as an optional worked example. Read the [FS1 research note](../../../research-notes/002-fs1-market-thermometer/README.md) for the archived evidence. Keep the general research workflow independent of FS1.

The private price-to-axis implementation and raw datasets are not included. The public [reader](../scripts/read_fs1_audit.py) accepts an existing authorized audit export; it does not produce FS1 from OHLC or screenshots.

## 1. Define the observation object

Record symbol, broker/source, server timezone, observed span, actual history origin, indicator version and data mode. UNIVERSAL and LEGACY_XAU are different coverage pipelines.

If an authorized `Market_Fingerprint_v0_3_indicator.mq5` indicator, internal version 0.31, is already installed:

1. Select `InpDataMode = MP_UNIVERSAL`.
2. Set `InpShowDetails = true` to inspect raw values.
3. Set `InpExportAuditCSV = true`, keeping the intended history origin fixed.
4. Use `InpAuditCutoff = 0` for the latest completed server sessions; a historical cutoff must be a supported past/current server midnight.
5. Find `MQL5/Files/Market_Fingerprint_FS1_<SYMBOL>_universal_audit.csv` in the terminal's data folder after a successful rebuild.
6. Preserve history-loading, reconciliation and NA messages rather than shortening history until a desired color appears.

The display timeframe does not change the internal M1-to-M15/daily pipeline. The default history request starts at 2024.01.01; record the actual export span rather than assuming every file used that setting.

## 2. Read numeric State before the code

| Raw field | Meaning and units | Comparison prefix |
| --- | --- | --- |
| volatility | Percent-valued movement intensity | vol |
| trend | Unsigned dimensionless efficiency/persistence | trend |
| breakout | Percent-valued success rate under the existing event definition | breakout |
| meanrev | Percent-valued success rate under the existing event definition | meanrev |

Read the prefix's exported `_lag20`, `_delta20`, `_scale252` and `_z` fields. The volatility lag is `vol_lag20`, not `volatility_lag20`.

- Lag20 is the value 20 observation positions earlier, with missing rows retained.
- Delta20 is current minus lag. Percent-valued axes produce a difference in **percentage points**.
- Scale252 and z describe scaling of the **change**, not extremeness of today's raw level.
- D and Pulse describe change magnitude. Pulse is not a profit probability, a direction or an absolute cross-instrument scale.

A larger unsigned trend measurement can describe a more persistent rise or fall. Delta is an endpoint comparison, not a fitted slope or a current-tick direction.

## 3. Preserve quality and availability

Server day D is usable no earlier than D+1 at server midnight under the completed-session pipeline. The export has neither a collection timestamp nor a UTC offset. The reader's earliest-availability field is derived, not an observed collection time.

The `data_verified` flag comes from the exporter. Tick counts support broker-history reconciliation; they are not order flow. The reader does not independently inspect raw M1/M15/D1 history.

Retain NA rows and unverified observations. Do not zero-fill axes or collapse the timeline before computing lags. A ready fingerprint with missing Pulse is possible.

## 4. Run the public reader

From the repository root, with Python 3.9 or newer and no third-party packages:

~~~bash
python skills/market-state-measurement-first/scripts/read_fs1_audit.py Market_Fingerprint_FS1_XAUUSD_universal_audit.csv --output fs1_report.json
~~~

On Windows, `py` can replace `python`. Omit `--output` to print JSON. Use `--mode LEGACY_XAU` only for a declared legacy export; do not treat it as the same measurement coverage as UNIVERSAL.

The reader supports comma-separated UTF-8/UTF-8-BOM and UTF-16. It rejects malformed rows, invalid counts, nonfinite values, mixed/unexpected modes and non-increasing dates. It reports lag, delta and fingerprint mismatches using the export's own cuts. Equality at a cut stays on the lower bit.

Exit 0 means the implemented export checks passed. Exit 2 means rejection or inconsistency. This does not certify raw-feed completeness, historical scaling/Pulse calculations or predictive ability. Whole missing sessions need an external calendar check.

| JSON field | Interpretation |
| --- | --- |
| export_data_verified_rows | Count of exporter flags, not independently audited sessions |
| fingerprint_NA_rows | Missing labels retained in the timeline |
| axis_support | Available/missing values and observed ranges |
| latest_observed_row | Last input observation, even when unverified or incomplete |
| error_count and first_errors | Failed check count and the first 25 details |

The script operates locally and makes no network calls.

## 5. Read a concrete archived example

On the last common export day, 2024.06.28:

| Field | XAUUSD | EURUSD |
| --- | ---: | ---: |
| volatility | 1.406744 | 0.561747 |
| vol_lag20 | 1.438156 | 0.421164 |
| vol_delta20 | -0.031411 | +0.140583 |
| fingerprint | FS1-F02 | FS1-F02 |

Volatility was below its 20-observation reference in XAU and above that reference in EUR. The figures do not identify an external cause. The same code can hide meaningful numeric differences.

These exports end in June 2024 and are **not current market readings**. Each file retained 20 initial NA labels. All coded EUR rows had the low volatility bit, showing a limitation of the fixed cut in that sample.

## 6. Return a bounded report

Return the actual observation object and clock; quality and missingness; raw values, lags, deltas and units; an optional code after the values; evidence status; and the limits of the interpretation.

If only a news narrative or chart impression is supplied, label the numeric market-state claim **UNMEASURED** and identify the required price/export data. Do not invent percentages of news influence. If a required FS1 input is absent, report it rather than substituting a new estimator and calling it FS1.

Without the private exporter, use the general workflow with separately declared metrics. FS1 is an example, not a mandatory formula.

## 7. Reading guide in Thai

เริ่มจากข้อมูลและค่าดิบ ไม่เริ่มจากสี ถ้ามีไฟล์ audit ให้ใช้สคริปต์ตรวจ แล้วอ่านว่าสี่แกนมีค่าเท่าไร เปลี่ยนจาก 20 observations ก่อนเท่าไร และข้อมูลพร้อมแค่ไหน ค่าเปอร์เซ็นต์ลบกันได้เป็นจุดเปอร์เซ็นต์ ส่วน Trend วัดความต่อเนื่องแบบไม่บอกทิศขึ้นลง

F00 ถึง F15 เป็นรหัสย่อ ไม่มีลำดับดีหรือแย่ และ NA ไม่ใช่ F00 สองตลาดมีรหัสเดียวกันแต่ค่าดิบและการเปลี่ยนต่างกันได้ Pulse อ่านขนาดความเปลี่ยนเมื่อเทียบประวัติของตลาดนั้น ไม่ใช่โอกาสกำไร

ถ้ายังไม่มีข้อมูลวัด อย่าสรุปว่าข่าวมีอิทธิพลกี่เปอร์เซ็นต์จากความรู้สึก ให้ระบุว่า UNMEASURED ก่อน สกิลช่วยจัดลำดับวิจัย เครื่องอ่าน CSV ช่วยตรวจไฟล์ที่มีอยู่ ส่วนสูตรสร้าง FS1 จากราคายังอยู่ในงานต้นฉบับ
