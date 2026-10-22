# FS1 UNIVERSAL as a Market Thermometer

**Miller & Lunar Research — Public Research Note 002**  
**Documentation edition v1.2 | 2026-10-22 | Not peer reviewed**

This is **Research Note 002, not Paper 002**. It documents an existing measurement tool and archived outputs. It adds no market experiment, forecasting test, strategy gate or parameter search.

## Abstract

FS1 UNIVERSAL describes market behavior numerically before optionally compressing four State axes into a fingerprint. The measurements concern movement intensity, directional persistence, breakout-event follow-through and mean-reversion-event behavior. Separate fields compare the measurements with the instrument's own earlier observations.

This note connects the [measurement-first skill](../../skills/market-state-measurement-first/SKILL.md) to an actual export schema. It reviews the existing source and two archived exports, explains State, change and code, and supplies a public CSV reader. The private price-to-axis implementation remains outside this release.

The exports contain 643 XAUUSD observations and 647 EURUSD observations, ending on 28 June 2024. Their lag references, delta arithmetic and fingerprints pass the reader's checks. These checks do not independently reconstruct the measurements from raw market data or establish predictive ability.

## 1. The bounded question

The thermometer asks: **what do the declared market measurements say, and how have they changed under the same pipeline?**

Measure that change before asking whether news, an election or monetary policy explains it. An AI estimate that news explains some percentage of a chart is not measured attribution merely because the answer contains a number.

FS1 does not establish external causation, the next price direction, state persistence or a strategy's profitability. No such test is added here.

## 2. Keep State, change and code separate

| Output | Meaning | Boundary |
| --- | --- | --- |
| Four raw State axes | Numerical market behavior under the declared pipeline | Not a complete description of a market |
| Lags, deltas, standardized change and Pulse | Comparison with the instrument's own history | Not a probability of profit or an external explanation |
| FS1-F00 through FS1-F15 | Four-bit compression relative to exported fixed cuts | No good/bad, bullish/bearish or safety ordering |

Each of the four axes contributes one binary bit according to whether its value is strictly above its exported fixed cut. Four binary axes produce `2^4 = 16` possible combinations, encoded as `FS1-F00` through `FS1-F15`; equality with a cut remains on the lower bit.

The raw fields are `volatility`, `trend`, `breakout` and `meanrev`. Volatility, breakout and mean reversion use percent units. Trend is an unsigned, dimensionless efficiency/persistence readout; a larger trend value does not distinguish an upward from a downward path.

The `*_delta20` fields are current minus the value 20 observation positions earlier. Differences in percent-valued fields are **percentage points**. This is an endpoint comparison, not a fitted slope or an intraday change.

The `*_scale252` and `*_z` fields concern the **20-session change**, not the extremeness of today's raw level. `D` summarizes standardized change across the axes. Pulse ranks that change magnitude against the instrument's own preceding history. Pulse 80 in two instruments does not imply equal absolute volatility.

### Why Pulse starts much later than the fingerprint

The core has two sequential historical windows. First it scales the 20-session deltas using **252 preceding delta observations**, excluding the current one. It then computes D and requires **252 preceding D values**, again excluding the current one, before producing Pulse.

| First possible output with adequate event support and complete data | Zero-based index | One-based row |
| --- | ---: | ---: |
| All four State axes | 20 | 21 |
| All four delta20 fields | 40 | 41 |
| Scale252, z and D | 292 | 293 |
| Pulse | 544 | 545 |

Thus the earliest possible Pulse needs **545 observations**, not merely lag20 plus one 252-row window. The reviewed exports reach those first positions: 643-544 = 99 available Pulse values in XAU and 647-544 = 103 in EUR. Missing inputs, inadequate event support or a zero MAD scale can postpone readiness further. These positions describe the existing calculation; no warm-up rule was changed.


## 3. Pipeline and availability

The reviewed source is `Market_Fingerprint_v0_3_indicator.mq5`, internal version **0.31**. It derives M15 and daily observations from M1 history. The display chart timeframe does not replace this internal pipeline.

UNIVERSAL reconciles M1 aggregates with native broker M15 and D1 OHLC and tick counts. Tick counts check consistency; they are not order flow or a fifth axis. Reconciliation within a broker's history does not certify accuracy against an independent market feed.

Observations use the broker's server-day boundary. Under the completed-session pipeline, day D is usable no earlier than D+1 at server midnight. The CSV supplies `server_day`, not a collection timestamp or UTC offset. This derived earliest boundary does not prove that a reading was collected on time.

`LEGACY_XAU` is the older XAU-specific coverage/profile retained from earlier FOUR work. `UNIVERSAL` is the current default cross-symbol pipeline used in the reviewed FS1 work. The modes share the numerical core but differ in coverage rules, so identical FS1 codes should not be treated as directly interchangeable across modes. In the reviewed UNIVERSAL implementation, M1-derived observations are reconciled with broker-native M15 and D1 history.

Retain missing and unverified observations in the timeline. Do not drop them before computing row-based lags, fill missing values with zero, or turn a missing code into F00. A fingerprint may be ready while Pulse remains missing.

## 4. Archived export checks

These are observed spans, not proof of requested terminal settings. The current default history request starts in January 2024, whereas these exported files contain earlier observations. Preserve actual configuration and observed span when comparing files.

**Configuration provenance is incomplete.** The exports carry data mode and cuts, but not the requested history start, audit cutoff, export time, broker timezone, producing source/build hash or configuration hash. The reviewed reference source is v0.31; the files themselves do not authenticate their producing build. The reader's input SHA identifies the CSV bytes, not the configuration that produced them.

Do not infer the requested history start from the first available row, retroactively insert today's defaults, or claim an old export now has a verified configuration. For future exports, those settings and identifiers should accompany the CSV in metadata or a sidecar record. That exporter change has **not** been implemented in this documentation release.

| Check | XAUUSD | EURUSD |
| --- | ---: | ---: |
| First observed server day | 2022.01.03 | 2022.01.03 |
| Last observed server day | 2024.06.28 | 2024.06.28 |
| Rows retained | 643 | 647 |
| Exporter flags data_verified=true | 643 | 647 |
| Available fingerprints | 623 | 627 |
| Fingerprint NA rows retained | 20 | 20 |
| Available Pulse values | 99 | 103 |
| Reader mismatches | 0 | 0 |

The last row in each export provides a common-date illustration, without selection by trading outcome. Readouts below are rounded.

| Readout on 2024.06.28 | XAUUSD | EURUSD |
| --- | ---: | ---: |
| Volatility percent | 1.406744 | 0.561747 |
| Trend efficiency | 0.002443 | 0.206502 |
| Breakout percent | 52.272727 | 51.515152 |
| Mean reversion percent | 21.476510 | 20.379147 |
| Volatility delta20 in percentage points | -0.031411 | +0.140583 |
| Pulse | 15.476190 | 63.492063 |
| Fingerprint | FS1-F02 | FS1-F02 |

Both labels are F02 despite different raw values and opposite signs of volatility change. The code is a coarse index, not an equivalence claim. F00 is likewise a combination relative to cuts, not a danger label.

The reviewed implementation uses shared fixed display cuts in the axes' own units:

| Axis | Fixed cut | Bit weight |
| --- | ---: | ---: |
| Volatility | 2.0% | 8 |
| Trend efficiency | 0.25 | 4 |
| Breakout success rate | 50.0% | 2 |
| Mean-reversion success rate | 25.0% | 1 |

A bit is 1 only when its raw value is **strictly greater** than the cut. These are common numerical display boundaries, not instrument-specific percentiles, a market-derived universal calibration or selected trading gates. The recovered source states that they are fixed and not recalibrated to EA results. **The original empirical rationale/calibration history was not recovered**; this edition cannot establish whether the choices were initially motivated by XAU.

Identical codes across instruments therefore assert only the same four inequalities against these cuts, not equivalent relative market states. The numeric values and within-instrument changes remain the main comparison surface.

All 627 coded EURUSD rows had the low volatility bit in this export. The fixed volatility cut therefore did not distinguish high and low groups there. This is a limitation of that display boundary in this sample, not permission to tune it against trading outcomes. No cut was changed for publication.

### Event rates need their own reference

Breakout near 52% and mean reversion near 21% are conditional success rates under their respective existing event definitions and horizons. They are not directly comparable to each other, a 50/50 coin flip or unconditional random-candle behavior.

No matched base rate under the same event definitions is reported here. Consequently these readouts describe observed behavior; they do not establish excess continuation, unusually weak reversion or a trading edge. A stronger comparison needs a separately declared reference process or sample, not a benchmark chosen after seeing these rates.

## 5. A practical public handoff

Use the [general skill](../../skills/market-state-measurement-first/SKILL.md), [worked example](../../skills/market-state-measurement-first/examples/fs1-universal.md) and [CSV reader](../../skills/market-state-measurement-first/scripts/read_fs1_audit.py).

The reader accepts an authorized existing FS1 export. It checks schema, date order, count bounds, mode, lag/delta arithmetic and the fingerprint against cuts supplied by the file. It preserves missing rows and reports the last observed row without replacing it with an earlier valid observation.

It does not calculate FS1 axes from OHLC or recompute historical scaling and Pulse. Without the private exporter, use the general workflow with separately declared measurement definitions. Matching column names does not establish FS1 compatibility.

## 6. Evidence boundary and provenance

**MEASURED:** archived fields, spans, counts and the implemented export checks. The exporter supplies the data-verification flag; the public reader does not independently audit broker history.

**NOT TESTED BY THIS RELEASE:** prediction, external causation, return relationships, strategy gates, and generalization across all instruments or brokers.

This publication adds no MetaEditor compile, new MT5 runtime run or independent raw-data replication. Missing whole sessions require an external session calendar to detect; ordered dates alone do not establish completeness.

Reviewed inputs:

1. `Market_Fingerprint_v0_3_indicator.mq5`, internal version 0.31, for field semantics, time boundaries, modes and export schema.
2. `Market_Pulse_v0_2_Guide_TH.md`, for earlier coverage and validation explanations, retaining its original version-specific limits.
3. `Market_Fingerprint_FS1_XAUUSD_universal_audit.csv`, 643 rows.
4. `Market_Fingerprint_FS1_EURUSD_universal_audit.csv`, 647 rows.

The indicator implementation, raw market data, full audit datasets and private source locations remain in the research archive. Selected derived readouts and the independent CSV-reading utility are public. This supports inspection of the workflow and export checks, not full public reconstruction of FS1.

Software tests use fabricated audit rows to check missing values, encoding, equality at a cut, corrupted labels/deltas, mixed modes, duplicate dates and an unverified latest observation. These are parser tests, not market experiments.

FS1 remains a small descriptive thermometer. This release adds no forecast, state taxonomy, axis, optimized threshold or order execution. Future Paper 002 remains separate.

| Edition | Date | Change |
| --- | --- | --- |
| v1.0 | 2026-10-22 | Documented the existing thermometer, reviewed two archived exports and added a CSV reader. No new market run or changed measurement rule. |
| v1.1 | 2026-10-22 | Editorial clarification only: explained the four-bit/16-code encoding and distinguished the archived LEGACY_XAU profile from the reviewed UNIVERSAL cross-symbol pipeline. No measurement rule, threshold, result or conclusion changed. |
| v1.2 | 2026-10-22 | Documented the two-stage warm-up and first possible Pulse at row 545; exposed fixed cuts with unknown calibration provenance; identified missing export configuration/build metadata and the absence of matched event base rates. No exporter or measurement change. |

Prepared by **Miller & Lunar Research** through a human-directed research workflow with AI-assisted code, analysis and editorial support. See the repository's attribution and rights boundary.
