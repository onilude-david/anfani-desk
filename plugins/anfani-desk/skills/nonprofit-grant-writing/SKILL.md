---
name: nonprofit-grant-writing
description: "Drafts letters of inquiry (LOIs) and full grant proposals for foundation, government, and corporate funders: needs statements, program narratives, budget narratives, evaluation/logic-model summaries written for a specific funder's guidelines, and grant reports. Use when a user asks to write or edit an LOI, draft a proposal narrative or budget narrative, respond to a specific RFP/NOFO's required sections, or write a grant report to a funder. Does not cover finding or vetting funders, tracking RFP deadlines, or scoring funder fit (use nonprofit-grant-research), and does not cover building the underlying logic model or theory of change from scratch (use nonprofit-program-design) — this skill packages an existing program design into funder-ready language."
license: MIT
metadata:
  supervision: "review"
  supervision_note: "Proposals are binding representations to a funder about what you will deliver."
  date_added: "2026-09-07"
  date_added_source: "git:1860ed47a83901ff5e6d45abc4a2ef05be8fd4cd"
---

# Grant Writing: LOIs, Proposals & Reports

## When to Use This Skill

Use this skill once a funder has been identified and you are producing the written application or
report itself. For finding/vetting the funder, tracking deadlines, or scoring fit, use
`nonprofit-grant-research` first. For building the logic model or theory of change this proposal
will describe, use `nonprofit-program-design` first — this skill assumes that design work exists
and focuses on translating it into funder-ready narrative and budget language. Typical triggers:

- "Write a letter of inquiry for [funder]"
- "Draft the program narrative for this RFP"
- "Write a budget narrative justifying these line items"
- "Turn our logic model into a proposal's outcomes section"
- "Write our year-end grant report to [funder]"
- "Edit this proposal down to the funder's word/page limit"

## Standard Proposal Structure

Most funder applications map onto this sequence even when section names vary; use it as the
default skeleton and then re-map to the funder's exact required headers:

1. **Executive summary / cover letter** — one paragraph each on: who you are, the problem, the ask
   amount, and the expected outcome. Written last, read first.
2. **Statement of need** — the problem, backed by data specific to your service area (not national
   statistics alone), told with urgency but without exploitative framing (dignity-preserving
   framing guidance lives in `nonprofit-storytelling`; apply it here).
3. **Program description / methodology** — what you will do, drawn directly from the program's
   logic model (activities and outputs); name the model type if funders expect it (e.g.,
   evidence-based, evidence-informed, promising practice).
4. **Goals, objectives, and outcomes** — objectives should be SMART (Specific, Measurable,
   Achievable, Relevant, Time-bound); outcomes map to the logic model's outcome tier, not just
   activities. Distinguish outputs (units of service delivered) from outcomes (change achieved).
5. **Evaluation plan** — how outcomes will be measured, what data collection tools, and reporting
   timeline; keep this consistent with whatever the org actually tracks (coordinate with
   `nonprofit-outcomes-measurement` rather than promising a measurement approach the org can't
   execute).
6. **Organizational capacity** — track record, key staff bios, relevant past grants delivered
   successfully.
7. **Budget and budget narrative** — see below.
8. **Sustainability plan** — how the program continues after this grant period (diversified
   funding, earned revenue, embedded costs).

## Letters of Inquiry (LOI)

An LOI is a 1-2 page gate before a full proposal invitation. Include: brief org description,
problem statement (2-3 sentences), proposed project and amount requested, alignment to the
funder's stated priorities (cite their specific language), and one differentiator. Cut everything
that would appear in the full proposal — an LOI's job is to earn the invitation, not tell the whole
story.

## Budget Narrative

A budget narrative justifies every line item in the budget spreadsheet in prose, tied to the
program description:

- State the basis for each figure (e.g., "0.5 FTE Program Coordinator at $58,000 annual salary +
  22% fringe = $35,380") rather than a bare number.
- Separate direct and indirect costs and state the basis for any admin or overhead line (a percentage of
  direct costs, named). The US federal indirect-cost rules in the original skill (2 CFR 200) were removed
  from this bundled copy; if a US federal award applies, read the original at the URL in SOURCE.md. Flag restricted expense categories and any cap the funder states.
- Reconcile the requested amount against the total project budget — clearly show what other
  revenue sources cover the balance if this grant is partial funding.

## Concrete Steps

1. Read the RFP/NOFO or funder guidelines in full before drafting; extract every required section
   header, word/page/character limit, required attachments, and submission mechanics (portal,
   email, hard deadline time zone).
2. Confirm the program design/logic model source material exists and is current; if not, route to
   `nonprofit-program-design` before drafting outcomes language.
3. Draft in the funder's required order and exact section names, even if it differs from the
   skeleton above — reviewers score against their own rubric, not general best practice.
4. Write the statement of need with locally specific data and named sources.
5. Draft goals/objectives as SMART statements distinct from activities.
6. Build the budget narrative line-by-line against the numeric budget; reconcile totals and match
   the indirect rate, base, and cost period to finance's approved calculation. Keep unresolved rate
   assumptions visibly marked for review rather than presenting them as approved.
7. Trim to the funder's word/page/character limit — cutting adjectives and repeated context first,
   never cutting the ask amount, outcomes, or evaluation plan.
8. Route for internal review: program staff check factual/programmatic accuracy, finance checks
   the budget, ED or board chair signs off on institutional commitments before submission.
   Escalate unresolved Federal rate, base, or applicability questions to the qualified reviewer
   required by `nonprofit-cost-allocation`; ordinary proposal drafting remains staff-reviewed.
9. Submit ahead of the deadline accounting for portal upload time and required attachments
   (W-9, 501(c)(3) determination letter, board list, audited financials, org chart).
10. On award, calendar the reporting schedule and build the report from the same
    outcomes/evaluation language promised in the proposal — do not let the report drift from what
    was funded.

## Grant Reports

Structure interim/final reports around the original proposal's stated objectives: report progress
against each SMART objective, actual spend against the approved budget (flag and explain material
variances), a challenges/lessons-learned section (funders read this for candor, not just success
stories), and specific plans for the next period if renewal is possible.

## Common Failure Modes

- **Recycled boilerplate**: submitting the same narrative to every funder without mapping to their
  specific stated priorities and section names — lowers scoring even when the program itself is
  strong.
- **Outputs mislabeled as outcomes**: "served 200 clients" is an output; "72% of clients improved
  reading level by one grade" is an outcome — funders increasingly require the latter.
- **Budget-narrative mismatch**: numbers in the narrative don't foot to the attached budget
  spreadsheet — always reconcile before submission.
- **Mishandling restrictions**: ignoring a valid expense restriction, or accepting a conflicting
  Federal indirect-cost cap without checking its authority; resolve with finance before submission.
- **Missing attachments**: technically compliant narrative but incomplete required-attachments
  checklist, causing an administrative rejection regardless of narrative quality.

## For Advisors

When brought in to strengthen a client's win rate, first audit 3-5 recent declined proposals for
pattern failures (funder-fit misses vs. narrative weakness vs. missing evaluation rigor) rather
than rewriting prose on instinct — that diagnostic belongs partly to `nonprofit-grant-research` if
the pattern is fit, and to this skill if the pattern is narrative/outcomes clarity. Coach staff to
separate program description from evaluation language, since conflating the two is the most common
weakness advisors see in client-drafted narratives. Recommend a standing "boilerplate library"
(mission, org history, capacity statements) maintained centrally so writers spend their drafting
time on the funder-specific need/outcomes sections that actually move scores.

