# The Payout Gap: A Retrospective Case Study of Trading Returns, Account Rules, and Cash-Flow Claims

**Miller & Lunar Research — Paper 001**  
**Public Working Paper v1.0 | 2026-10-11 | Not peer reviewed**  
**Research disclosure:** Human-directed research program with AI-assisted analysis and editorial drafting. Quantitative examples come from a private historical archive; original strategy trade-generation and external firm-rule execution have **not** been independently replicated. This public copy omits proprietary source files and private research links. It does not document actual trader income.

## Abstract

Profitable historical trading results, rule-constrained account survival, opportunities to request a payout, receipt of modeled cash, and a trader's net business income describe different outcomes. This retrospective research-program case study examines how these distinctions emerged across successive, related trading-system experiments rather than treating any one strategy as the subject of the paper. An expanded-history reassessment of the FOUR portfolio illustrates how initial durability claims can weaken when the evaluation window changes; the documented methodological decision is available, but its full historical performance figures are not independently reconstructed here. The frozen Toy A+C portfolio provides an illustrative 238-day equity high-water-mark recovery episode, which is **not equivalent** to an interval without withdrawable cash. A separate, funded-only payout cohort export yields 169 calendar-eligible one-year starts, a median of seven recorded claims, and a median longest no-claim interval of 140.17 days; those archived claim ledgers were reconciled, not independently regenerated from market data. Single-start payout-policy and portfolio-family experiments further show that shorter modeled cash droughts need not produce higher receipts, while a separate Universal Breakout study documents why consistent realized-trade payouts cannot establish fund-rule execution compliance. The combined lesson is methodological: each business claim requires its own event clock, account-state model, versioned evidence, and cost ledger. Because samples, strategies, execution assumptions, and simulation versions differ, these related cases are **not independent replications** and do not establish a cross-firm real-world failure rate or net payout probability.

## 1. Introduction

Trading systems are often compared using cumulative return, expectancy, profit factor, and maximum drawdown. These measures can describe aspects of statistical performance, but they do not directly answer a different operational question: **when, and under what conditions, can the trader actually withdraw money?**

This distinction becomes especially important in prop-firm evaluation programs. A trader may have to reach an initial profit target, pass a second evaluation stage, avoid breaches of daily or total loss limits, and satisfy payout conditions before any cash is received. The trade sequence and starting date therefore affect the result. A strategy can have positive aggregate performance over the available historical sample and still experience long intervals without a payout—or fail a particular funded-account path before its longer-term statistical advantage has time to materialize.

The research problem is not to find a perfect entry rule or eliminate every flat segment of an equity curve. It is to distinguish a **profitable strategy** from an **economically usable payout process**. This is a problem of path dependence, risk budgeting, rule design, and accounting, not solely a problem of signal quality.

The unit of analysis in this paper is **a linked research program's evolving measurement and decision framework**, not the returns of a selected trading algorithm. FOUR, Toy A+C, funded-cashflow simulations, and Universal Breakout are embedded *examples of different questions*, with distinct data and evidential limits. When cases build on the same frozen signals or market history, they are connected observations, not independent corroborations. The research archive includes abandoned hypotheses and simulator corrections; we retain them to prevent hindsight selection and to document where an earlier inference ceased to be justified.

The archive is analyzed without retuning entries, exits, or portfolio weights for the sake of producing attractive paper results. Revising a conclusion when more history or better accounting becomes available is a finding about the evaluation method, not a license to retrofit trading signals.

**Reading contract for this working paper:** Each finding in §5 answers a bounded methodological question with a relevant recorded experiment, explicit evidence status, and a decision/limitation. Additional experimental or account-level testing is *outside* this internal retrospective manuscript; it would require a separate protocol and cannot be silently treated as work completed here.

## 2. Research question and scope

**Primary question:** What did this multi-stage research program reveal about the non-equivalence of backtest returns, equity recovery, account survival, payout events, and household economic viability—and where does the evidence stop?

**Secondary questions:**

1. Which concepts remain distinct even when the same strategy history produces all of the metrics?
2. Which archival counterexamples changed a research decision (for example after expanding sample history, correcting payout accounting, or changing the portfolio mix)?
3. Which quantities were actually measured, and what do the recorded start/end events mean?
4. Which additional data, rules, and costs would be required before making a claim about real prop-firm business viability?

The paper synthesizes **bounded, non-pooled case evidence** from several archived experiments with separately dated rule and cost assumptions. It does **not** claim that one firm's rules represent all firms, that historical performance predicts future withdrawals, or that a research-grade simulator is an execution-certified live trading system. A conclusion with no supporting ledger or source code is presented as a research decision or hypothesis—not as a verified numerical fact.

### 2.1 Relation to earlier literature

The central issue is **the estimand**, rather than a proposed new trading signal or a claim to have invented path dependence. Bailey, Borwein, López de Prado and Zhu (2017) formalize a framework for evaluating backtest overfitting, which is relevant to selecting a strategy using inspected history. Goldberg and Mahmoud (2017) and Maier-Paape and Zhu (2018) study drawdown-based risk measurement, helping distinguish equity-path risk from other objectives. Kaplan and Meier (1958) provide a foundational treatment of incomplete time-to-event observations; here, a terminated or not-yet-completed payout path similarly requires an explicit censoring boundary, although this paper **does not estimate a Kaplan–Meier survival curve**.

These sources do not by themselves imply that conventional drawdown metrics are invalid, or that they assume unlimited capital. Rather, **return, drawdown and expectancy alone cannot certify event-defined payout eligibility, external cash receipt, or cumulative net business break-even**. The six-clock table is offered as a practical synthesis for this study, **not as a proven first-in-literature invention**.

## 3. Conceptual framework

### 3.1 Statistical edge

Statistical edge describes an observed favorable performance tendency under a defined sampling, cost, and risk convention. Positive historical total R alone does not establish forward durability or a reliable cash withdrawal schedule.

### 3.2 Account survival

Survival is compliance with the simulated account's loss and operational rules throughout a particular lifecycle. A favorable unconditional return distribution can coexist with account breaches on some start dates because limits apply to the **path**, not merely the endpoint.

### 3.3 Payout continuity: eligibility, claim, modeled settlement and actual receipt

Payout continuity concerns **declared payout-related events**, not an equity high-water mark. At least four distinct states may matter: (i) account or trade **eligibility** under a defined rule; (ii) a recorded **claim/request** made once required conditions hold; (iii) a simulator's **modeled payout completion/receipt** after an assumed delay and account replacement; and (iv) a **verified external transfer** arriving in the trader's possession. A fifth, distinct business question asks when those transfers exceed all external costs.

These states form a conceptual event sequence, **not** an assertion that every account must follow the same mandatory payout workflow. For example, Gate 1R counts recorded *claims* in already-funded synthetic cohorts, while CR2R/CR2F record **modeled external receipt timestamps**, under explicit assumed settlement and account-replacement rules. The UB closed-trade replay answers still another, more limited simulated-payout question. None of these archives establishes the date of a real bank transfer.

Possible metrics include time from cohort start to first recorded claim, elapsed time between matched claims, time from funded start to modeled receipt, fraction of eligible cohorts with at least one event inside a specified horizon, and the longest interval lacking that **specified event type**. A longest high-water-mark underwater interval and a longest no-claim or no-receipt interval are **different constructs**, and even *claim gap* and *cash receipt gap* cannot be interchanged unless the same event semantics and start/end boundaries are demonstrated.

### 3.4 Business viability

Economic viability requires tracking the trader's own cash flows: evaluation and reset costs, payout amounts after any firm split, fees, and calendar time. Gross simulated account profit is not automatically the same as positive net income for the trader.

### 3.5 Six non-interchangeable clocks

To make a payout-timing statement meaningful, both the **start event** and **end event** must be declared. In particular, *first external payment received* and *external business break-even* are not the same endpoint.

| Clock | Start event | End event | Business interpretation |
| --- | --- | --- | --- |
| Backtest recovery | Prior equity high-water mark | New high-water mark | Recovery of recorded strategy equity, **not** time to cash |
| Funded cohort-to-claim | Already-funded simulated account start | Recorded eligible payout claim | Funded account claim timing, excluding purchased evaluation and bank settlement |
| First-trade-to-claim | First executed trade | First recorded claim | A separate first-payout clock even within the same funded cohort export |
| Funded start-to-modeled receipt | Already-funded simulated start | Modeled cash-received event | Simulated settlement/wait; no purchased evaluation or verified bank transfer |
| Household purchase-to-first-receipt | First external evaluation fee paid | First **verified** outside cash receipt | First real money back, **not necessarily break-even** |
| Household purchase-to-break-even | First external evaluation fee paid | First instant cumulative net outside cash reaches zero or higher after the initial outlay | Recovery of invested external cash, including documented fees and payouts, **not measured** in this archive |

The final two clocks are **unobserved** in the reconciled funded-only datasets. They must remain separate even when the same household ledger can eventually calculate both.

For ordered payout-event timestamps \(t_1, \ldots, t_n\), with a declared start \(t_0\) and observation end \(T\), one possible **longest no-payout interval** is

$$
G_{\max} = \max\big(t_1-t_0,\;t_2-t_1,\;\ldots,\;t_n-t_{n-1},\;T-t_n\big).
$$

When \(n=0\), the observed gap is \(T-t_0\). For an account that fails or whose data are truncated, \(T\) must be the **declared observation/termination boundary**; any resulting tail interval is censored and is not evidence of what would happen after termination. The selected Gate 1R export uses **cohort start** for \(t_0\) in its longest-gap calculation, while its separate `first_payout_days` field counts from **first trade**. The selected CR2R case instead timestamps **modeled external cash receipt**. Substituting one for another changes the estimand.

### 3.6 Payout is not household profit

A business ledger must keep separate the simulated account profit, any claimed/distributed trader share, the actual date of receipt, and all money contributed from outside the account. Define **first actual receipt** as the earliest verified incoming transfer following an initial external purchase. Define **first net break-even** as the earliest later time at which cumulative net external cash is at least zero **after recording the initial purchase and all applicable outlays**. A positive first incoming transfer may still leave the household cumulatively negative. Conceptually, household net cash at date \(T\) is

$$
C_{\mathrm{net}}(T)
= \sum_{k:\,t^{\mathrm{received}}_k\leq T} \mathrm{cashReceived}_k
- \sum_{j:\,t^{\mathrm{paid}}_j\leq T} \mathrm{externalFeeOrCost}_j.
$$

Evaluation fees, reset fees, replacement purchases, and other real outlays belong to the second term only if they are actually applicable and documented. It would be a category error to compute a "profitable prop-firm business" from **gross strategy R** or **already-funded modeled reward dollars** while treating unknown external costs as zero.

## 4. Retrospective case-study method and provenance

### 4.1 Embedded cases and frozen baselines

The research program contains several embedded cases, each included **because it exposes a distinct measurement or decision problem**, not because one is the definitive winning algorithm:

- **FOUR long-history reassessment (FOUR-HISTORY):** a methodological negative case about sample-window durability, broker/environment sensitivity, and reversing an earlier deployment interpretation. Its original trade-level results are not independently audited for this manuscript.
- **Toy portfolio construction (TOY-AC-D):** tests the distinction between standalone positive performance and portfolio utility. The archived frozen A+C portfolio consists of Donchian trend breakout A and EMA200/RSI(2) trend-aligned pullback C at 50/50; D was a separate, ultimately rejected positive standalone candidate for that portfolio role. Numerical claims remain checkpoint-level until frozen ledgers and code match.
- **Funded-account timing (AC-GATE1R, AC-CR1/CR2R/CR2F):** related A+C-derived experiments on claim clocks, cash accounting, harvest policies and family reallocation. Selected archived payout exports were reconciled, but **no evaluation-purchase-to-real-bank-receipt path** is verified.
- **Execution admissibility (UB-V02):** a separate system demonstrating why modeled payouts from closed-trade records do not prove synchronized floating-equity, margin, order lifecycle or actual firm compliance.

The cases must retain their experiment IDs, source dates, original risk budgets, and version-specific limits. None is a universal baseline for all the other cases. Entry, exit and weights were not retuned to improve this manuscript.

**Version exclusion identified in the archive.** A separate older document titled `pattern A` (private archival record) discusses A+B and gives A **564 trades / +38.42R**; it is *not* the accepted Qwen A+C baseline, whose archived preflight identity is A **876 trades / +107.15R**. The `Pattern C` document (private archival record) is useful for its strategy description, but its included example script has not been independently matched to the frozen trade outputs. These historical sources must not be treated as interchangeable evidence solely because they reuse the letter "A".

### 4.1.1 Authority hierarchy and why identity must be frozen

The 2026-09-10 authoritative research handoff (private archival record) explicitly distinguishes a later Qwen baseline from preliminary Jamie calculations. The earlier changing Pattern A results (564 trades / +38.42R in one document and 863 trades / +105.74R in another calculation round) were classified as **non-authoritative**. The baseline accepted for this archival case instead identifies A with **876 trades / +107.15R** and C with **1,333 trades / +22.40R** over IC XAUUSD H1 history to September 2026.

For the present paper, source priority is: (i) accepted frozen trade identities and executable manifests where available; (ii) event-level or cohort-level archived exports matching those identities; (iii) explicit dated checkpoint narratives that describe decisions and limitations; (iv) exploratory notebook illustrations. An attractive chart or reprinted strategy label does not override a mismatched run identity. The separately authored Pattern C strategy note (private archival record) contains historical Python examples, but these have **not** been shown to exactly reproduce the accepted frozen Qwen ledger. The case study therefore uses Qwen's archived identity as a *reported baseline*, not as an independently verified code-level reproduction.

### 4.1.2 Evidence types are not interchangeable

The historical record has three distinct strengths: (i) **decision checkpoints** that establish what the team knew and why it changed direction; (ii) **summary reports and locked-run identities** that describe specific historical experiments; and (iii) **export-reconciled payout events**, for which already-generated CSV ledgers were checked arithmetically. A fourth level—original code and market-data replication—has not been completed across the program.

A research decision to exclude a strategy after a broader history test is genuine archival evidence of a *changed decision*. It is **not** evidence of any precise out-of-sample loss probability until the longer-history numeric ledger is audited. Similarly, a claim ledger agreeing with its summary is evidence of **internal reconciliation**, not proof that an external provider would permit those payouts.

### 4.1.3 Chronology of changes in what the researchers were willing to claim

This is a **reconstructed chronology of archived research decisions**, not a prospective study design. The dates identify surviving checkpoints or reports; the earlier history of each strategy often extends beyond the date of the document.

| Research episode / dated archive | Question that changed | What the archive allowed the researchers to conclude | What this paper does *not* infer |
| --- | --- | --- | --- |
| **September 10 — FOUR extended-history reassessment** (handoff (private archival record)) | Would earlier confidence survive a wider window? | Its long-horizon durability thesis was **downgraded**; do not rescue with a retrospective regime patch | A verified cross-era failure rate or precise performance estimate |
| **September 10 — Toy A+C/D** (same handoff (private archival record)) | Can a positive standalone component improve or hurt the portfolio? | Reported marginal contribution and HWM path, not just total component R, determined whether D filled its proposed role | That Toy returns are independently rerun here, or that the Toy HWM is a payout clock |
| **September 12 — FTMO viability prototype** (checkpoint (private archival record)) | Does account survival solve cash timing? | Distinguished equity recovery from no-payout drought, keeping execution and swap assumptions visible | A completed, verified real purchased-evaluation-to-bank-receipt lifecycle |
| **Gate 1R / 1R-A — cohort/account audit** (report (private archival record), audit (private archival record)) | Were denominators, withdrawal DD and daily loss treated correctly? | Corrected selected 14D model accounting and preserved the 30D semantics concern as a hold | That a coded daily-loss proxy is a firm's validated real breach result |
| **CR1 / CR2R / CR2F — payout policy and family probes** (CR2R report (private archival record), CR2F report (private archival record)) | Do cycle replacement, harvesting or reallocation improve cash timing? | Reconciled payout-event arithmetic exposed different timing/amount trade-offs on the declared modeled paths | A universal portfolio ranking or actual bank settlement |
| **September 16 — UB admission review** (checkpoint (private archival record)) | Does a coherent closed-trade payout replay establish live viability? | Deployment remained **INSUFFICIENT EVIDENCE** without synchronized account floating equity, margin and order lifecycle | That UB's signal economics were disproven or that deployment was certified |

This sequence motivates the *cross-case questions* in §5 but is not a claim that all changes were generated by one common dataset or that the findings form a controlled experiment.

### 4.1.4 How a research question became a test and then a decision

The case-study record is organized as an **observable inference and decision trail**, not as a reconstruction of participants' unrecorded internal thoughts. For each case, the editorial sequence asks: **(1) What was the practical problem? (2) Which working assumption made a proposed metric or experiment appear useful? (3) What comparison or change was actually made? (4) What did the recorded output show? (5) What conclusion was retained, rejected, or suspended? (6) What evidence would be needed for a stronger claim?** A question or assumption that cannot be established from a dated artifact is marked as editorial interpretation rather than attributed retrospectively to the team.

Three documented transitions illustrate this approach:

| Problem and working rationale in the archive | Actual test or audit and reported observation | Revised decision and boundary |
| --- | --- | --- |
| **Equity recovery versus income continuity:** Toy A+C had a recorded 238-day longest high-water-mark recovery interval, but a prop-firm operator needs to know *when an account can make a payout claim*. | The September 12 funded-viability checkpoint (private archival record) explicitly separated HWM recovery from payout drought; later Gate 1R exported calendar-start claim events and gaps for a different, already-funded model. | Measure payout claims on their own chronological account path. **Do not** treat the 238-day HWM observation as 238 days without a claim, and do not claim the two reported gaps describe the same matched cohort. |
| **Positive component versus useful diversification:** Toy D was positive standalone in the September 10 handoff (private archival record), but the portfolio question concerned its contribution during A+C weaknesses, not just its own aggregate R. | The first A/C/D weight comparison reduced C's role disproportionately. The team corrected the comparison to a documented A:C-preserving 37.5/37.5/25 mix. The corrected checkpoint reported longer HWM recovery and lower aggregate R than A+C. | Reject D **for that assigned portfolio role** without attempting to rescue it by parameter search. The test does not prove that D can never be useful in another system; these numbers remain checkpoint-level pending source-ledger replay. |
| **Apparent payout success versus account feasibility:** The UB v0.2 checkpoint (private archival record) retained a payout simulation even after fixing entry-freeze/flat-recheck behavior. | The corrected closed-trade replay could be internally reconciled, but did not reconstruct synchronized shared-account **floating drawdown**, margin and pending-order lifecycle. | Mark fund admission **INSUFFICIENT EVIDENCE**, rather than promoting UB as execution-ready or claiming its historical signal edge was refuted. |

These transitions are examples of **why the measurement design evolved**, rather than a claim that the entire research program was specified prospectively. We preserve negative results, version disagreements, and the moment an earlier inference was withdrawn. The manuscript uses dated documents to evidence those transitions; it does **not** invent a pre-test hypothesis where none was recorded.

### 4.2 Strategy layer and account-state layer are distinct

We examined existing research artifacts for whether they kept **trade-generation outcomes** separate from **account lifecycle outcomes**. The archived Toy baseline supplies historical strategy-level results, while Gate 1R and CR2R/CR2F report funded-account cash and payout-state simulations built around related signals. An earlier September FTMO prototype described Challenge and Verification stages but is *not* promoted here as a fully independently verified end-to-end implementation. UB used a different closed-trade ledger and payout replay. These are different evidentiary objects; the current retrospective synthesis does not newly connect them into one validated full lifecycle.

The analytic requirement for any future complete account model is to follow stage transitions in chronological order rather than multiply challenge, verification and funded success fractions as if stages were independent.

### 4.3 Cohort eligibility, comparison unit and censoring

The Gate 1R export has weekly funded-account start dates. We filtered the **BASELINE_AC / BASE_COST / 14D_FULL** experiment to starts with a full 365-day observation window, giving 169 eligible starts out of 221 generated start dates. We compared each selected cohort row with its exported payout events, including beginning-of-window intervals and the interval to the observation endpoint. These starts overlap heavily in calendar time, so their 169 modeled paths are **not** independent replications or 169 individual investors.

CR2R and CR2F instead each use one declared start date, January 28, 2023, with a January 28, 2024 observation end. Their final incomplete account cycles were not granted imaginary future payout events. In all cases, reported payout-event intervals are conditional on that simulation's event conventions; an incomplete tail is observed/censored at the stated endpoint.

### 4.4 Execution and account-rule assumptions

The source experiments employ different environment and execution proxies. The early viability model mixed period-specific market data with assumed spread, slippage and swap stresses; the CR2R/CR2F payout experiments use prepared H1 trade identities with retained M15 observation marks and a simulated bank-receipt delay, not historically observed receipt transactions. The code audit labels the $20 qualification as an **assumed closed-profit minimum for a selected bank-wire channel**, not a verified processing *fee* or a universal bank-transfer threshold.

The research archive also documented a payout/daily-loss-floor interaction that can create a modeled loss-limit violation without a new trading loss. We therefore do not interpret unverified 30-day Gate 1R survival rows as real rule failures. Original broker feed, historical swap, margin/floating-equity reconstruction, timezone resets and exact current firm rules remain non-equivalent across cases and unverified for deployment.

### 4.5 Observed outcomes versus unanswered economic outcomes

This retrospective analysis extracts the outcomes **actually available** in archived exports: historical portfolio R and equity recovery from checkpoints; count, size and intervals of simulated funded-account payout claims from Gate 1R; and modeled cash receipt events from CR2R/CR2F. Comparison rows are not treated as a new randomized experiment, and policy outcomes are explicitly labeled single-start where applicable.

The primary **unobserved** endpoints are full evaluation purchase-to-real-bank-receipt probability, cumulative external fees and reset purchases, confirmed live intratrade rule compliance, and net external household return. A methodology for measuring those endpoints can be specified, but they must not be reported as completed empirical results here.

### 4.6 What this manuscript actually verified

This is **archival case-study analysis**. Existing descriptive reports and checkpoints were read; selected existing exported CSVs were filtered, summed, and reconciled against their own recorded cohort/receipt events. Specifically, the Gate 1R payout count, reward amount and longest-gap calculations matched the 169 eligible start-date rows of the 14-day funded-account export, and the CR2R and CR2F completed-cycle payout sums matched their branch summaries. This is an **export-level consistency check** and does not independently establish that the source code generated legitimate signals, that intratrade losses were measured accurately, or that a real firm would admit and settle each claim.

The starting calendar dates, market feed, experimental policy, strategy version, and *the event used for each timing metric* are specified per experiment below. Cases are intentionally not pooled or treated as independent samples. The available evidence does not support estimating a single all-program failure probability or an unconditional fee-to-first-bank-deposit rate.

## 5. Findings organized by question, not by trading system

**Evidence status.** Each finding below is tied to its *measurement distinction* and one or more relevant cases; examples share neither a single experimental population nor a single verification level. The payout-ledger cross-check (private archival record) covers selected existing funded-only exports; FOUR and Toy strategy performance remain checkpoint-level. The research unit is the **program's accumulated knowledge and falsifications**, not a new pooled backtest of multiple systems.

### 5.0 Findings-to-evidence map (distinct samples, no pooling)

| Question / finding | Example from the research program | What the archive supports now | Evidence boundary |
| --- | --- | --- | --- |
| Is historical edge automatically durable across market eras? | FOUR-HISTORY | The September 10 review **downgraded** its earlier long-horizon/deployment thesis after expanding historical coverage | Dated decision checkpoint; exact multi-year numbers not reconstructed for this paper |
| Is standalone profit the same as useful portfolio diversification? | TOY-AC-D | D's checkpoint-reported standalone +9.60R did not improve the reported A+C diversification comparison; role was rejected | Checkpoint-level Toy outcome, no new ledger/code replay |
| Does an equity HWM recovery gap equal a cash gap? | TOY-AC and AC-GATE1R | A+C's reported longest HWM recovery was 238 days; a **different** funded cohort sample measured claim-gap distributions | Different event clocks and samples; not a matched 238-day cash comparison |
| Do payout summaries need repaired denominators and loss accounting? | AC-GATE1R/1R-A/CR1 | 169 calendar-eligible cohort starts reconciled for the 14D scenario; a 30D account-floor issue remained held | Export arithmetic, not validated external fund loss-floor semantics |
| Can risk/cash policies or mixing improve one metric while worsening another? | AC-CR2R/CR2F | One-start harvest and family variants changed payout timing and amounts in opposite directions | Cycle payout exports reconciled; not general strategy rankings |
| Does a reconciled payout simulation prove deployability? | UB-V02 | Corrected payout simulation still received an **INSUFFICIENT EVIDENCE** fund-admission decision | Separate closed-trade study without verified shared floating DD / order lifecycle |
| Is modeled payout income household business profit? | Across all cases | The archive explains required fees/receipt accounting but does **not** verify a net purchase-to-cash lifecycle | **Unmeasured**; no profit/ROI claim permitted |

The paper's examples have **different underlying strategies and overlapping market histories**, and some are downstream policy variations on the same strategy. The map is a guide to mechanisms, not a sample of independent successes or failures.

### 5.1 Apparent durability can change when the historical window expands (FOUR-HISTORY)

The September 10 research handoff (private archival record) records a reversal in the assessment of FOUR: an earlier description treated the pack as implementation-complete and usable, but a longer-history IC Markets review exposed earlier weak/negative stretches and concentration of returns in later years. The dated decision was to **downgrade its durability/deployment thesis** and treat FOUR as a methodological specimen rather than a candidate to rescue with retrospectively chosen regime filters.

This example supports a rule for evaluating evidence: broaden the historical sampling window before assuming an apparently attractive recent equity path is robust. It also warns that broker feeds, delay, lot quantization and minimum-capital effects can alter execution. However, the handoff expressly says its precise annual figures require a source-file/script audit; the manuscript therefore **does not reproduce the checkpoint's approximate longer-history drawdown as a verified numerical estimate**. The issue illustrated here is *durability and evidence-selection bias*, not an observed payout drought for FOUR.

### 5.2 Positive standalone returns do not guarantee marginal portfolio utility (TOY-AC-D)

The same Toy research handoff (private archival record) documents two different lessons. First, the A+C 50/50 combination had a reported +64.78R total, -11.56R maximum drawdown and 238-day HWM recovery interval, while its components could individually undergo longer weak periods. Its methodological point is that *timing and portfolio utility* cannot be inferred from standalone performance alone.

Second, the volatility compression/release candidate D was **positive standalone** in the archival Toy results (+9.60R reported) but worsened the comparison when fairly reweighted with A and C: the 37.5% A / 37.5% C / 25% D configuration recorded +50.98R versus A+C's +64.78R, about the same reported maximum drawdown (-11.57R versus -11.56R), and a longer HWM underwater interval (406 versus 238 days). The archive's decision was to *reject D for that particular portfolio role*, not to claim D is universally unprofitable.

These are **checkpoint-reported Toy figures**, with full independent ledger/code reproduction still open. They explain why the relevant selection criterion can be marginal portfolio contribution and timing, without asserting that portfolio diversification automatically improves real payout frequency.

### 5.3 Equity recovery time is not payout timing (TOY-AC / AC-GATE1R)

As shown in §5.2, the September 10 Toy research handoff (private archival record) reports a **238-day longest equity high-water-mark recovery interval** for the frozen, 50/50 XAUUSD H1 A+C portfolio over 2022–September 2026. That is a checkpoint-reported *strategy-equity measure*, not the duration of any one funded account's inability to request or receive a payout.

The September 12 FTMO viability checkpoint (private archival record) modeled a lifecycle with distinct evaluation/funded risk settings and cost scenarios. Its originally reported payout timing was explicitly described as a *research-grade prototype*, with historical swap unavailable and M15 floating-equity/reset timing not certified. It should not be presented as a validated estimate of live FTMO reward frequency or fee-to-first-cash economics.

**Documented reasoning transition.** The original practical objective moved from keeping a funded account alive to generating usable cash regularly. That change makes HWM recovery a potentially useful description of the return path, but not the correct dependent variable for a cash-flow decision. The September 12 checkpoint (private archival record) states this distinction explicitly; the subsequent claim-cohort models are **one way** the research program pursued it. This is an archived rationale, not proof that every payout must be mechanically independent of equity recovery.

**Interpretation:** the historical A+C result is a *checkpoint-reported example* of return and equity recovery. It cannot by itself tell us when a funded account claims a payout. Source-trade identity remains to be independently reproduced before a stronger empirical result is claimed.

### 5.4 Payout cohorts require correct denominators and loss accounting (AC-GATE1R)

The initial Gate 1 cash-flow anatomy outputs were **not decision-grade**. The Gate 1R repair specification (private archival record) identifies two errors: a 365-day cohort denominator that depended on survival, and spurious drawdown induced by cash withdrawals. The Gate 1R acceptance checks (private archival record) report repairs and deterministic fixtures passing. The restored calendar rule yielded **169 complete-year-eligible starts from 221 weekly starts** for each specified combination, independent of outcome. Withdrawal-normalized drawdown used account equity *plus cumulative withdrawals* to avoid treating a payout as a trading loss.

As an illustration only, the Gate 1R report (private archival record) shows in **BASELINE_AC | BASE_COST | 14D_FULL | complete_365d** a median **7 simulated payouts per eligible year** and a median **140.17-day longest no-payout gap**. The archived cohort and claim ledgers (private archival record) have now been checked: all 169 eligible start-date rows reconcile on payout counts, claim dollars, and longest payout gap, with one eligible cohort showing no payout. **A subtle but crucial definition:** `first_payout_days` is measured **first trade → first simulated claim**, while `longest_no_payout_gap_days` begins at **cohort start**. Neither measures evaluation purchase → actual bank receipt. This starts from an **already-funded modeled account**, so it is not proof of complete business viability. The 14-day recurring claim cadence is a *research policy*, not a statement that FTMO mandates repeat withdrawals every 14 days; overlapping weekly-start cohorts are correlated.

Even a locally internally consistent report can have a critical unresolved rule interpretation. The Gate 1R-A code/state audit (private archival record) documented a 2023-03-31 withdrawal that reduced raw account equity to $100,000 while leaving a daily-loss floor of $100,195.31 until the next reset. The subsequent proxy check recorded a breach of $195.31 *without an intervening trading loss*. The code behaved as implemented, but the external reward/daily-floor semantics were not established. Therefore **Gate 1R 30-day survival comparisons were put on hold**; one must not silently describe them as observed account failures or repaired live-rule outcomes.

### 5.5 Cash policy changes alter the lifecycle, not merely the equity curve (AC-CR1/CR2R)

The CR1 patch notes (private archival record) report passing deterministic fixtures for payout idempotency, entry freeze, fresh-account initialization, and persistence of household cash across account replacement. This was a **separate patch copy**; it did **not** rerun or overwrite the Gate 1R historical cohort batch, so the corrected local account-cycle logic must not be retroactively assigned to that earlier table.

A later CR2R single-start report (private archival record) compared two defined payout/harvest policies on the **same 2023-01-28 to 2024-01-28 timeline** for the same baseline and modeled costs. Archival reported values:

| One-start research scenario | Completed payouts | Modeled cash received | First modeled cash received |
| --- | ---: | ---: | ---: |
| CONTROL_14D_FULL | 6 | $7,417.24 | 18.42 days |
| HARVEST_2P50 (freeze and exit at +$2,500 net liquidation proxy) | 3 | $6,102.46 | 45.88 days |

The archived cycle ledger (private archival record) was directly reconciled: six Control reward rows sum to $7,417.2412, while three Harvest reward rows sum to $6,102.4622; both match the corresponding summary rows with no cash residual. The **longest observed receipt-to-receipt interval** was approximately **251.83 days for Control**, versus **260.23 days for Harvest** in this particular sample; each path also contains a censored final tail. A policy designed to harvest at +$2,500 did **not** ensure a shorter maximum cash drought here. Here the Harvest policy **froze new entries after each target trigger**, but did not reduce aggregate exposure time across the entire one-year run; it produced **fewer payout events, less modeled cash, and later first cash** than the control. The report attributes long waits mainly to time before the target was hit, rather than modeled processing. The study was **not** an optimization of the $2,500 threshold, did not include evaluation-purchase costs, and did not constitute a broad rolling-start trial. It assumed a $20 **closed-profit minimum** for a project-selected bank-wire channel (not a verified processing fee), two-business-day modeled receipt/replacement waiting, omitted historical swap, and used thinned M15 proxy observations. It is an example of why a plausible rule change does not automatically improve business cash flow.

**Minimum-transfer sensitivity.** The CR2R source-ledger audit (private archival record) also found that Control's first modeled receipt was only **$16.15** after its 80% split, against a **$20.19** gross claimable profit and a project assumption described as a "$20 closed-profit" minimum. That is compatible with applying the minimum *before* the share, but not proof of an actual payment-channel minimum after the split. Since the real-world qualification basis is unverified, both the count of first payouts and the first-cash timing should be treated as model-dependent rather than certified transfers.

### 5.6 A shorter cash drought can be bought at lower cash receipts (AC-CR2F)

The CR2F one-start family comparison (private archival record) fixed the same historical start date and one-year market timeline and compared two portfolios at equal nominal risk: XAU A $250 + XAU C $250 versus XAU A $200 + XAU C $200 + US100 C $100. The archived cycle ledger cross-check (private archival record) now reconciles all six completed receipt events for each branch.

The family shortened the longest modeled no-receipt interval from **251.83 to 207.63 days** (44.21 days shorter). Yet modeled cash received fell from **$7,417.24 to $4,571.22** ($2,846.02 less), and first cash arrived **21.17 days later**. Both branches had six completed receipt cycles and one unfinished cycle at the end. The cycle-level maximum drawdown proxy was lower for the family ($4,547.68 vs $5,975.02). Equal nominal risk was achieved through reallocation, not by adding extra US100 risk on top.

This is an export-reconciled **timing-versus-amount trade-off**, not a universally superior composition. The report's original operational label, CR2F_FAMILY_HURTS, applies only to its one-start decision criteria. The CR2F report explicitly did **not** generate a new large account-event file or regenerate source signals; its six modeled receipt events per branch were instead reconciled in the retained summary/cycle exports. It also did not provide multi-start confirmation, purchased evaluation fees, or live firm-compliance proof.

### 5.7 A reconciled payout ledger does not establish fund-rule execution feasibility (UB-V02)

The UB Final Admission v0.2 checkpoint (private archival record) and summary (private archival record) concern a **different strategy, timeframe experiment, historical period, and payout replay**. Its v0.2 simulation corrected entry freeze and already-open-position settlement, superseding earlier v0.1 results. Even after its event-ledger consistency checks, the team classified funded-account approval as **INSUFFICIENT EVIDENCE** because synchronized floating-equity DD, pending-order behavior, execution equivalence, and shared-account margin were not recoverable from closed trades. These UB results must **not** be pooled with A+C or the FTMO case-study results.

The methodological relevance is limited but important: **a reconciled realized-trade cash ledger does not establish intratrade account-rule compliance**.

### 5.8 Payout receipts are not a measured net household business (PROGRAM-BUSINESS)

**Timing precision:** The first modeled receipt clock is not the *first actual transfer* clock; neither establishes net household break-even. The current examples stop before those real-world endpoints.

The case studies distinguish account claim, assumed receipt, and externally paid evaluation costs, but no audited program-wide record here starts with a real purchased evaluation and follows **Challenge → Verification → Funded → verified bank receipt → cumulative net break-even**. Consequently, even the exact arithmetic reconciliation of the CR2R/CR2F models does not show that any purchased prop account would pay for itself, how many resets could occur, or the trader's return on actual cash spent. This is a deliberately documented **evidence gap**, not evidence that prop trading necessarily loses money.

## 6. Discussion — synthesis across related case studies

This research program exposes a sequence of **different failure points for inference**, not proof that any one trading system must fail:

1. **Generalization failure (FOUR).** A recently attractive equity curve is not proof that the same economics hold under broader history, alternate broker conditions or real execution.
2. **Portfolio-objective mismatch (Toy A+C/D).** Standalone positive expectancy and diversification usefulness are different measures. A combination that improves recorded equity drawdown or HWM recovery has not thereby established more timely payouts.
3. **Clock mismatch (A+C funded payout cohorts).** A 238-day HWM recovery period is not automatically 238 days without payout; payout eligibility and cash events require their own state machine. The available HWM and payout summaries arise from *different measurement runs*, so they are not a direct matched comparison.
4. **Accounting and policy-state mismatch (Gate 1R/CR1/CR2R/CR2F).** Whether a cohort remains in a denominator, whether a withdrawal is a loss, when an account resets, and whether an entry is suppressed can determine the reported outcome. Harvesting or reallocating changes both timing and cash.
5. **Execution admissibility mismatch (UB).** Accurate closed-trade reward arithmetic cannot show tick-level shared floating drawdown, margin occupancy, order cancellation, or compliance with a firm's trading restrictions. The correct research verdict can be *insufficient evidence* rather than declaring a strategy either proven viable or refuted.
6. **Personal economics mismatch (all cases).** A simulated gross claim and an actual net business are different objects. Program fees, resets, splits and bank receipt dates must appear in an external cash ledger before any break-even claim.

A useful study-design implication is to **choose the metric after stating the trader's objective**, and to preserve unflattering counterexamples. If the objective is time to first *actual* household cash receipt, the test starts from the first fee and follows verified incoming payment, not from an already-funded account. If the objective is time to **net break-even**, the model must additionally accumulate all external costs and receipts until cumulative net cash reaches zero. If the objective is survival, a 14-day claim-frequency proxy alone is insufficient. If the objective is long-run portfolio utility, its contribution through adverse windows matters as much as standalone total R.

The cases are deliberately neither pooled nor counted as independent confirmations: A+C, Gate 1R, CR2R and CR2F share strategy ancestry; FOUR and UB differ in design, history, risk assumptions and available execution data. The manuscript's contribution is an auditable **measurement taxonomy plus bounded case history**, not a statistical estimate of how often all profitable trading systems fail prop-firm programs.

## 7. Limitations and threats to validity

The available experiments vary in instrument, baseline strategy, years, cost models, risk grids, payout cadence and lifecycle stage. They are not a meta-sample. This is a retrospectively selected sequence of cases from a single research program, which is valuable for methodological tracing but not representative of the trading-system population. In particular:

- Overlapping start-date cohorts are not independent observations.
- Current swap values were used for stress in one early prototype, while other reports omitted historical swap.
- M15 close/retained proxy timelines cannot certify tick-level floating equity, spread spikes, or exact loss-reset compliance.
- Some assumed reward processing/receipt times, channels and payout cadence are not verified firm requirements.
- Original Gate 1 data defects and the later Gate 1R-A rule-semantics question must remain visible in the audit trail; CR1 corrected **a separate account-cycle patch** only.
- A system's historical test sample may already have been inspected during system selection, creating selection/overfitting risk.
- Broker feed, timezone/DST, lot rounding, margin and live manual-order feasibility can change the deployable path.
- No numerical 'failure to profit' claim should be extrapolated from these illustrative archived figures to future trader income.

## 8. Conclusion — bounded to verified evidence

The retrospective research program supports a common analytical distinction, not a universally validated payout prediction: **strategy return, portfolio utility, equity recovery, survival under account rules, payout claims, modeled receipts, and trader net business income are different objects**. Historical simulator revisions and changing research decisions show why each must be defined, versioned and audited. The *methodological case-study* findings can be reported at their stated evidence levels; a claim about real prop-firm profitability or program-wide rates would additionally require validated source-level trading paths, genuine account-state and firm-rule semantics, and net external cashflows from purchase through receipt.

## Evidence access, ethics and disclosure

The named experiments (FOUR-HISTORY, TOY-AC-D, AC-GATE1R, AC-CR2R/CR2F and UB-V02) are identifiable **within the authors' private, dated research archive**. The underlying strategy code, raw tick/bar data, brokerage/account identifiers, and internal Google Drive documents are **not** published here. Selected payout exports were reconciled against their own event and summary rows in the internal record, but this is not an independent reproduction of their source algorithms. Consequently readers cannot currently independently reproduce the exact reported performance examples from this publication alone. The numerical examples should be treated as **illustrative archived case observations** with the evidence classifications in §4.6 and §5.0, not as confirmed live-trading results.

The work was prepared in a human-directed research workflow supported by AI tools for code assistance, analysis, editorial drafting and critical review. An informal AI-assisted critique informed release edits; it was **not** external academic peer review. The project deliberately retains unfavorable results, uncertainty and unverified assumptions rather than retrospectively optimizing away contradictions.

No personal financial receipts, purchased-account cost ledger, or actual bank-deposit evidence are released or claimed. This text does not constitute investment advice or a performance advertisement.

## References

1. Bailey, D. H., Borwein, J. M., López de Prado, M., & Zhu, Q. J. (2017). *The probability of backtest overfitting*. **Journal of Computational Finance**. [https://doi.org/10.21314/JCF.2016.322](https://doi.org/10.21314/JCF.2016.322).
2. Goldberg, L. R., & Mahmoud, O. (2017). *Drawdown: From practice to theory and back again*. **Mathematics and Financial Economics, 11**, 275–297. [https://doi.org/10.1007/s11579-016-0181-9](https://doi.org/10.1007/s11579-016-0181-9).
3. Maier-Paape, S., & Zhu, Q. J. (2018). *A general framework for portfolio theory. Part II: Drawdown risk measures*. **Risks, 6**(3), 76. [https://doi.org/10.3390/risks6030076](https://doi.org/10.3390/risks6030076).
4. Kaplan, E. L., & Meier, P. (1958). *Nonparametric estimation from incomplete observations*. **Journal of the American Statistical Association, 53**(282), 457–481. [https://doi.org/10.1080/01621459.1958.10501452](https://doi.org/10.1080/01621459.1958.10501452).

**Version policy:** This release is a separately edited public copy of an internally frozen archival manuscript dated 2026-10-11. Future material changes should be recorded as a new public version; the private archival copy is not modified.
