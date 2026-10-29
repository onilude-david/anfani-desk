---
name: review
description: Independent reviewer-style critique of a filled application - run in a fresh agent that did not write it, return a verdict, the three fixes that matter most and the one question a reviewer would ask.
argument-hint: "<path to answers.md>"
---

# Review an application

Review: $ARGUMENTS

Run the review in a **fresh subagent** (general-purpose) that did not write the draft, so it reads like a stranger.
Give it the sheet, the programme's scoring criteria quoted in the sheet, and these instructions:

- Read as a reviewer with about a minute per application. Does the first sentence of each answer answer the
  question? Is every claim specific, dated and checkable? Does each criterion get its own visible evidence?
- Use `${CLAUDE_PLUGIN_ROOT}/skills/opportunity-desk/references/field-guide/question-bank.md` (what each question
  type tests and the common mistakes) and, for startup programmes, the review rubric and red-flag checklist in
  `references/field-guide/yc/external-tools.md`.
- Check for AI tells: stacked threes, "not X but Y", empty openers and closers, inflated words, dashes as punctuation.
- Return: a verdict (STRONG / BORDERLINE / WEAK), the three fixes that would most change the outcome, the one question
  a reviewer would ask, and any claim that looks unprovable.

Then show the user the verdict and offer to apply the fixes. Ask for facts rather than inventing them. Stop after
three rounds. Log the review in the sheet under "Review log".
