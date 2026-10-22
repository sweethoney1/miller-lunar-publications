# FS1 UNIVERSAL — Worked Measurement Example

**Purpose:** show what a measurement-first market-state table can look like in practice.

This example is derived from archived FS1 UNIVERSAL audit exports for XAUUSD and EURUSD. It is intentionally limited to the public research lesson. The private source code, raw market data and implementation formulas are not published here.

FS1 should be read as a **market thermometer**, not a trading signal, forecasting engine or automatic strategy gate.

## 1. What gets measured

The current audit schema exposes four primary endogenous market-behavior axes:

| Axis | Research role |
| --- | --- |
| `volatility` | Measure the scale/intensity of price movement. |
| `trend` | Measure directional persistence rather than merely direction. |
| `breakout` | Measure breakout behavior / follow-through in the observed window. |
| `meanrev` | Measure mean-reversion behavior / retracement burden in the observed window. |

These names identify the measurement roles. This public example does **not** define the private implementation formulas behind each field.

The audit also stores event counts and success counts used by the implementation, including breakout and mean-reversion event fields.

## 2. Compare the state with its own history

A useful market-state measurement does not stop at today's absolute value.

The FS1 audit therefore keeps comparison fields including:

- `*_lag20` — the corresponding value from 20 sessions earlier;
- `*_delta20` — the change versus that 20-session reference;
- `*_scale252` and `*_z` — longer-horizon scaling / standardization fields when sufficient history is available.

This allows the research question to become more precise.

Instead of:

> “The market feels more volatile now.”

ask:

> “How much did the volatility measurement change relative to the same pipeline 20 sessions earlier, and how unusual is the current level within its longer history?”

## 3. Compress only after measuring

The audit contains a compact `fingerprint` field such as `FS1-Fxx`.

That label is **downstream** of the numeric measurements.

Correct order:

```text
price / event data
        ↓
numeric market measurements
        ↓
historical comparisons
        ↓
optional fingerprint label
```

Incorrect order:

```text
choose a market label
        ↓
search for numbers that justify it
```

A label is useful for communication and indexing. It is not evidence by itself.

## 4. Two-instrument sanity check

The archived UNIVERSAL audit was produced for both **XAUUSD** and **EURUSD** under the same output schema.

That does not prove universal validity across instruments. It demonstrates the research discipline being sought: use the **same camera** before comparing different markets or periods.

When adapting the workflow, keep definitions, timestamp handling, missing-data rules and causal availability consistent before interpreting differences.

## 5. How to use this example without copying FS1

You do not need FS1's private formulas to apply the method.

Choose a small set of measurements appropriate to your question. For example:

- realized range or dispersion for volatility;
- path efficiency or directional persistence for trend;
- continuation after a defined break for breakout follow-through;
- retracement depth or return-to-reference frequency for mean reversion.

Then freeze those definitions and create a table with one row per chosen observation period.

A minimal template:

| date | volatility | trend | breakout | meanrev | vol_delta | trend_delta | breakout_delta | meanrev_delta |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| t0 | ... | ... | ... | ... | ... | ... | ... | ... |
| t1 | ... | ... | ... | ... | ... | ... | ... | ... |

Only after that table exists should you ask whether a news, macroeconomic, political or other external variable explains the observed transition.

## 6. Evidence boundary

This worked example establishes only that the archived FS1 UNIVERSAL pipeline produces a consistent numeric market-state audit with the field families described above.

It does **not** establish that:

- the four axes are sufficient to describe every market state;
- the fingerprint labels predict returns;
- a particular fingerprint should enable or disable a strategy;
- the same thresholds are appropriate for every instrument;
- an external event caused any measured transition.

The reusable lesson remains:

> **Measure first. Explain later.**
