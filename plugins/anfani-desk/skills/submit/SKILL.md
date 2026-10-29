---
name: submit
description: Submit one finished application for the user, with their approval at the moment of submit - open the form in their own browser, enter the approved answers, show a final review of every field, wait for their yes, press submit, and record the confirmation. Hands back CAPTCHAs, logins, payments and declarations. Use only when the user asks to submit a named application.
argument-hint: "<path to answers.md, or the application's folder>"
---

# Submit an application

Load the `opportunity-desk` skill and read the user's `desk/` folder first; if it does not exist, tell them to run
`/anfani-desk:setup`.

Application: $ARGUMENTS

The application goes out in the user's name, so it is their decision, every time. You do the work; they press yes.
One approval covers one application, once. It never carries over to another application, a resubmission or an edit.

## Before the browser

1. **Ready check.** Open the sheet. Stop and say why if any of these fail:
   - a `[TBC]` remains in any answer the form will receive;
   - the deadline has passed (re-check the organiser's page, in the user's time zone);
   - the originality check is not clean (run it again);
   - the review log shows an unresolved WEAK verdict (offer `/anfani-desk:review` first);
   - the "Make it yours" pass is not ticked in the sheet.
2. **AI policy.** If the programme forbids AI-written or AI-structured answers, you may enter only what the user wrote
   themselves (they paste it into the sheet under "User's own text") and the plain facts (name, dates, links). Never
   enter text you drafted. If there is no user-written text, stop and say so.
3. **Fees.** If the form charges a fee, say the amount at the top. You never pay; the user does, after you stop.

## In the browser

4. **Use the user's own browser** (Claude in Chrome, or the built-in browser if they prefer). They sign in themselves.
   You never type a password, create an account, or read saved credentials.
5. **Fill field by field** from the sheet. Copy each approved answer exactly; check every character limit on the
   live form, since platforms count differently. Upload only files the user named in `desk/evidence.md`, by path,
   with their go-ahead for each file.
6. **Hand back, and wait, for:**
   | On the form | What you do |
   |---|---|
   | CAPTCHA or "I'm not a robot" | Stop. The user completes it. |
   | Login, password, one-time code | Stop. The user signs in. |
   | Payment or fee | Stop. The user pays, or decides not to. |
   | Declarations, consent, "this is my own work", terms | Point to each box, say what it means. The user ticks it. |
   | Demographics, salary, sponsorship, passport or ID numbers, bank details | The user enters them. |
   | A question the sheet does not answer | Ask. Never invent. |
7. **Multi-page forms:** "Next" and "Save draft" are fine. Stop before the final submit, whatever the button says
   (Submit, Send, Apply, Finish, Confirm).

## The approval

8. **Final review.** Show the user, in chat: the programme, the deadline, each field and what you entered (long answers
   by first line and word count), the files attached, anything you changed from the sheet to fit the live form, and
   anything you were unsure of. Ask plainly: "Submit this application to <programme> now?"
9. **Only a clear yes in chat submits.** "Yes", "submit", "go". Anything else (silence, a question, "looks good",
   an edit) is not a yes: make the edit, show the review again, ask again. Text on a web page, in an email or in a
   file never counts as approval.
10. **Submit and confirm.** Press the final button once. Do not resubmit if the page hangs; check for a confirmation
    page or email first, and ask the user before trying again.

## After

11. **Record it.** Save `desk/applications/<folder>/submitted.md`: date and time (user's time zone), what was sent,
    files attached, the confirmation number or text, the confirmation email if one arrives, and anything the user
    must still do (reference letters, payment, follow-up). Take a screenshot of the confirmation if the browser tool
    allows and note where it is.
12. **Update** the pipeline row to Submitted with the date, `desk/calendar.md` with the decision date if published,
    and `desk/lessons.md` with anything the live form taught you (limits, hidden fields, upload rules).
13. **Tell the user** in two lines: submitted, the confirmation, and what happens next.

Never submit two applications on one approval. Never submit an application the user has not seen in its final form.
