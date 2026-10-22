# Research Handoff

**Release 2026-10-22-review-1**

Use this file as the entry point for the publications and reusable workflow. Component edition numbers describe separate documents; they are not intended to match each other.

## Component map

| Component | Current edition | Read |
| --- | --- | --- |
| Paper 001 The Payout Gap | v1.0 | [Paper](papers/001-the-payout-gap/working-paper-v1.0.md) |
| Research Note 001 The Dinosaur Accident | v1.3 | [Dinosaur](research-notes/001-the-dinosaur-accident/README.md) |
| Research Note 002 FS1 thermometer | v1.2 | [FS1](research-notes/002-fs1-market-thermometer/README.md) |
| Measurement-first skill | Workflow snapshot in this release | [SKILL.md](skills/market-state-measurement-first/SKILL.md) |
| FS1 worked example | v1.3 | [Example](skills/market-state-measurement-first/examples/fs1-universal.md) |
| FS1 CSV reader | Utility snapshot in this release | [read_fs1_audit.py](skills/market-state-measurement-first/scripts/read_fs1_audit.py) |
| Reader software tests | Synthetic parser fixtures | [Tests](tests/test_fs1_audit.py) |

See [CHANGELOG.md](CHANGELOG.md) for the changes grouped by release. Research Note 002 is not the planned Paper 002.

## Obtain a working copy

Download the whole repository using GitHub's **Code → Download ZIP**, or clone the repository, and preserve its folder layout. The relative links and commands refer to those canonical paths.

Do not flatten the repository into renamed 00–04 Markdown files. A handout that omits the Python reader is a reading extract, not a runnable export-checking package. Previously distributed renamed handouts have not been inspected or repaired by this release; obtain a fresh whole-repository copy instead.

## Use the workflow

Start with the skill and one bounded question. If an authorized FS1 audit is available, follow the worked example to read raw State, lag/delta, missingness and the optional fingerprint. If no numerical data are available, report the claim as UNMEASURED and identify the missing inputs rather than inventing numerical attribution.

From the repository root, using Python 3.9 or newer:

```bash
python skills/market-state-measurement-first/scripts/read_fs1_audit.py YOUR_AUTHORIZED_FS1_AUDIT.csv --output fs1_report.json
```

The input filename above is a placeholder for the reader's own file. On Windows, `py` can replace `python`. The script uses the Python standard library and does not make network calls.

To run the included software tests:

```bash
python -m unittest discover -s tests -v
```

The tests use fabricated audit rows. They check the utility, not market predictability.

## Reproduction boundary

The public reader is included. The full private XAUUSD/EURUSD audit inputs and the indicator implementation are not included. The published zero-mismatch counts were checked against those private archived exports; access to this repository alone does not let a reader reproduce those particular counts or reconstruct FS1 from raw OHLC.

The public utility can inspect an authorized existing export, and its parser behavior can be checked with the included synthetic tests. A reader can also apply the general measurement-first workflow with separately declared metrics. These are distinct uses.

## Scope of this correction

This release clarifies existing definitions and reports additional descriptive arithmetic from the frozen C55 ledger. It does not rerun market data, retune a strategy, construct a null distribution, estimate confidence intervals, create event base rates or modify the private exporter.

Unknown historical configuration and cross-project holdout usage remain explicitly unknown. See the combined changelog for the review items that remain outside this release.
