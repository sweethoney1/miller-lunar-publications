---
name: market-state-measurement-first
description: Use when investigating why a trading strategy behaves differently across periods, when someone says the market has changed character, or when macro/news/regime stories are being proposed before the market-state change itself has been measured.
---

# Market-State Measurement-First

## Purpose

Prevent a research project from explaining a market change before it has defined and measured the change.

Core rule:

**Measure first. Explain later.**

This workflow is for research design. It is not a trading signal, regime classifier, forecasting model or automatic strategy gate.

## Use this skill when

Use it when the working question sounds like:

- Why did this strategy work in one year and fail in another?
- Has market structure changed?
- Is this a different volatility regime?
- Did an election, policy change, war, liquidity shift or macro event change the market?
- I have traded through every market condition; how do I encode that experience?
- Which market state makes this setup work?

## Do not start with a story

External variables may matter, but do not make them the first explanation unless they have already been operationalized.

Bad research order:

1. choose a narrative;
2. find a price window that looks compatible;
3. add features until the narrative appears true.

Preferred order:

1. observe a behavioral difference;
2. define the measurable object;
3. measure it consistently;
4. compare periods;
5. identify transitions/divergences;
6. test external explanations afterward.

## Step 1 — Freeze the question

Write one bounded question before analysis.

Examples:

- Which measured properties of XAUUSD H4 differ between 2024 and 2025?
- Do large structural trends show similar morphology across two years?
- Does a strategy's loss cluster coincide with a measured change in volatility, persistence or follow-through?

Do not combine “describe the state,” “predict the state,” and “trade the state” in one stage.

## Step 2 — Define the observation object

Declare:

- instrument;
- source;
- time span;
- timeframe or source-row basis;
- bar aggregation;
- timestamp convention;
- missing-data policy;
- causal availability rule.

A market state cannot be compared if the camera changes between periods.

## Step 3 — Measure endogenous market behavior first

Choose the smallest defensible measurement menu for the question.

Possible families include:

- volatility / range / dispersion;
- directional displacement;
- path efficiency or persistence;
- expansion versus contraction;
- breakout follow-through;
- retracement or mean-reversion burden;
- structural-event density;
- duration / occupancy of directional states;
- unresolved / neutral-state coverage.

Do not include every available feature simply because it exists.

## Step 4 — Separate description from selection

If studying “large moves,” define the population using variables native to that timeframe.

Do not let a downstream entry setup define the population and then claim the setup was discovered inside it.

Freeze parent identities before descending to lower timeframes.

## Step 5 — Compare periods under one definition

For each measured field report:

- support;
- missingness;
- distribution;
- direction and magnitude of change;
- rank/correlation stability when relevant;
- whether the relationship keeps or reverses sign across periods.

Do not treat “looks similar” as sufficient when the research question requires measurement.

Do not treat “I have experienced all market conditions” as a quantified regime definition.

## Step 6 — Identify transition before cause

A transition claim needs an observable change point or a defined comparison.

Keep three statements separate:

1. **Observation:** market behavior differed.
2. **Association:** an external variable moved with it.
3. **Causation:** the external variable produced the change.

Never promote statement 1 or 2 into statement 3 without additional evidence.

## Step 7 — Only then test external explanations

After the market change is measurable, external variables can be tested.

Examples:

- policy-rate changes;
- inflation;
- macro surprises;
- liquidity proxies;
- event windows;
- election or geopolitical periods.

Ask whether they:

- precede the measured transition;
- coincide with it;
- explain incremental variance;
- generalize outside the originally noticed episode.

A plausible historical story is not automatically a mechanism.

## Step 8 — Protect the holdout

If a future or withheld period exists:

- freeze definitions first;
- record hashes/specifications where practical;
- open the holdout once for the declared question;
- do not rescue a weak result by changing thresholds after inspection.

If the holdout has already been used elsewhere, say so. Do not call it pristine.

## Evidence labels

Use explicit labels:

- **MEASURED** — directly computed under a declared definition.
- **CROSS-PERIOD RECURRING** — relationship repeated under the same definition across declared periods.
- **PROSPECTIVE SUPPORT** — a frozen hypothesis received support on a predesignated later partition.
- **ASSOCIATION ONLY** — variables move together; causation not established.
- **HYPOTHESIS** — plausible explanation not yet tested.
- **UNMEASURED** — claim currently based on impression/narrative only.
- **NOT SUPPORTED** — declared test failed or contradicted the claim.

## Stop rules

Stop rather than expand the project when:

- the state cannot be defined without hindsight;
- a feature exists only because it looked good after outcome inspection;
- the same definition cannot be applied across periods;
- the parent market-state population changes when lower-timeframe results are opened;
- an external narrative is doing all the explanatory work;
- the question has silently changed from description to prediction or trading;
- additional features are being added only to rescue a weak result.

## Output template

Return:

### Research question
One sentence.

### Observation object
Instrument, source, timeframe, period and causal clock.

### Frozen measurements
Small declared feature set.

### Cross-period evidence
What remained stable, changed or reversed.

### Evidence status
MEASURED / CROSS-PERIOD RECURRING / PROSPECTIVE SUPPORT / ASSOCIATION ONLY / HYPOTHESIS / UNMEASURED / NOT SUPPORTED.

### What this does not prove
At least one explicit boundary.

### Next question
Only the next bounded question. Do not auto-start it.

## Example of correct sequencing

Observation:
A strategy performs very differently in 2024 and 2025.

Weak response:
“2024 was difficult because macro conditions were bad.”

Measurement-first response:
“Before explaining the difference, measure volatility, persistence, expansion/contraction, follow-through and retracement burden under one frozen definition. If a repeatable market-state difference appears, then test whether macro variables explain it.”

## Provenance note

This workflow was distilled from the Miller & Lunar Research “Dinosaur” lineage, where an entry-search project changed direction after cross-year structural measurements produced a more interesting question than the original entry rule.
