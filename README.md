# Anfani Desk

**Your private opportunity desk, inside Claude Code.** It finds scholarships, grants, fellowships, awards,
accelerators, fully funded events, speaking slots and roles that fit you, checks your eligibility before you spend an
evening, fills applications from your real record in your own voice, and submits them when you say yes.

Made by [Anfani](https://anfani.app), the platform that finds the opportunities that suit you. Free and open source
(MIT).

## What it does

- **Scouts** in the order you care about (master's first, or grants first, or talks first), checks every deadline on
  the organiser's own page, and keeps a pipeline so nothing is checked twice.
- **Gates and scores.** Nationality, age, degree, fees, travel: a failed rule is a "no" with the reason, not a wasted
  evening. Pay-to-attend "scholarships" and vanity awards are flagged.
- **Fills applications** question by question: reads the form first, maps each scoring criterion to a true story and a
  fact, writes inside every limit, and marks anything only you know as `[TBC]`. A Word copy is saved beside each
  sheet.
- **Respects the rules.** Where a programme forbids AI-written answers (some scholarships do), it prepares your facts and
  leaves the writing to you. Every sheet passes an originality check so no paragraph is copied from anywhere.
- **Submits on your yes.** It fills the live form in your own browser, shows you every field, and presses submit only
  when you approve that application in chat. Then it saves the confirmation and updates your pipeline.
- **Learns.** Tell it outcomes and new facts in one inbox file; it updates your record and gets sharper each run.
- **Knows how programmes read.** A built-in field guide (researched October 2026 from about 470 sources) covers 83
  question types and how grants, scholarships, fellowships, awards, accelerators, jobs and calls for speakers are
  scored, plus a Y Combinator chapter.

## Install

You need [Claude Code](https://claude.com/claude-code).

```
/plugin marketplace add <owner>/anfani-desk
/plugin install anfani-desk@anfani
```

## Use

```
/anfani-desk:setup            # once: reads your CV, asks about 15 questions, builds your private desk/ folder
/anfani-desk:scout            # find what fits you now (or: /anfani-desk:scout master's)
/anfani-desk:fill <link>      # fill one application from your record
/anfani-desk:review <sheet>   # an independent reviewer's verdict and the three fixes that matter
/anfani-desk:submit <folder>  # fill the live form, show you the final review, submit on your yes
```

Or just talk to it: "scout for me", "is this worth my time?", "fill this application".

## Your data

Everything about you lives in `desk/` in your own project folder, on your computer: your profile, gates, priorities,
voice, stories, pipeline and applications. The plugin itself holds no personal data. Passport, ID and bank numbers are
never written into any file. Setup offers to add `desk/` to `.gitignore` so your record is never committed by
accident. Web searches are made to find and check programmes; what you share beyond that is up to you and the tools
you connect.

## How submitting works

1. The application is final: no `[TBC]` left, originality clean, your "Make it yours" pass ticked.
2. You open the form in your own browser and sign in yourself.
3. The desk fills each field from the sheet, then shows you everything it entered.
4. You say yes in chat. One yes submits one application, once.
5. It saves the confirmation in `submitted.md` and marks the pipeline row Submitted.

It hands back to you, and waits, for CAPTCHAs, logins, payments, declarations ("this is my own work"), and personal
fields such as ID numbers or salary. Where a programme forbids AI-written answers, it enters only text you wrote.

## What it will never do

Submit without your yes, register, create an account, sign in, solve a CAPTCHA, pay, tick a declaration for you, or
email anyone for you.

## Honest limits

- Deadlines and rules change. The desk re-checks each programme's own page, but always confirm before you submit.
- It is only as good as your record. Unknowns stay `[TBC]` until you answer them; it will not invent a fact.
- Not legal or immigration advice. For visas and entities, use a qualified adviser.

## Credits

Bundled MIT-licensed skills (see each folder's LICENSE and SOURCE.md): nonprofit-grant-writing,
nonprofit-program-design, nonprofit-outcomes-measurement, nonprofit-storytelling (Nonprofit Skills); impact-report and
scholarship-essay (Mohit Aggarwal); pitch-deck-mastery (Steve Kaplan); o1-case-strength-assessor (Claude for Legal
Contributors). The application-review rubric and mock-interview ideas in the YC chapter adapt MIT-licensed work credited
in `references/field-guide/yc/external-tools.md`.

## Licence

MIT. See [LICENSE](LICENSE).
