---
name: fill
description: Fill one application from the user's real record - read the form, map evidence, draft every answer in their voice inside the limits, mark gaps, run the originality check and save a Word copy. Does not submit; that is /anfani-desk:submit.
argument-hint: "<link to the call or form, or pasted questions>"
---

# Fill an application

Load the `opportunity-desk` skill and follow its Fill and Hand over steps exactly. Read the user's `desk/` folder
first; if it does not exist, tell them to run `/anfani-desk:setup`.

Target: $ARGUMENTS

1. Open the organiser's own page. Record deadline, offer, fee, eligibility, funding and the AI-use policy. Gate the
   opportunity against `desk/gates.md`; if it fails a hard gate, stop and say why.
2. Find the form's real questions. If the form needs a login, ask the user to paste or screenshot the questions; never
   sign in.
3. Create `desk/applications/<yyyy-mm>-<slug>/answers.md` from
   `${CLAUDE_PLUGIN_ROOT}/skills/opportunity-desk/templates/answer-sheet.md`. Fill the form read, the evidence map and
   every answer, using `${CLAUDE_PLUGIN_ROOT}/skills/opportunity-desk/references/field-guide/question-bank.md` for each question type and the chapter for the
   category.
4. Where the programme forbids AI-written answers, give the record and the checklist, and leave the writing to the
   user.
5. Run the originality check and the Word export from the skill's scripts. Add a pipeline row.
6. Hand over: the sheet path, the `[TBC]` list, the warnings, and the recommendation. When nothing is `[TBC]`, offer
   `/anfani-desk:submit` (the user approves the final form before it goes).
