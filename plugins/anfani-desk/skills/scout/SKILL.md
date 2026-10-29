---
name: scout
description: Find opportunities that fit the user - search by their priorities, verify each on the organiser's page, gate on eligibility, score, update their pipeline and report a shortlist. Optionally fill the top sheets.
argument-hint: "[category or focus, e.g. 'master's' or 'next 30 days'] [fill N]"
---

# Scout

Load the `opportunity-desk` skill and follow its Scout and Hand over steps exactly. Read the user's `desk/` folder
first; if it does not exist, tell them to run `/anfani-desk:setup`.

Focus: $ARGUMENTS (default: every category in `desk/priorities.md` order; deadlines in the next 75 days plus rolling;
plus anything in `desk/calendar.md` whose preparation should start now).

Delegate the search to the `anfani-desk:opportunity-scout` agent (always the plugin's own, never another agent of the
same name) when the scope is broad. Process `desk/inbox.md` first. Write a
pipeline row for everything you looked at, update `desk/calendar.md` and `desk/ready-kit.md`, and write lessons to
`desk/lessons.md`. If the user asked to fill N sheets, fill the top N by score plus bonus, then deadline, using the
Fill steps. Report: the shortlist table, sheets ready, the `[TBC]` list grouped, warnings (unverified deadlines,
fees, pay-to-attend, deadlines inside 7 days), and one line on what to chase next. Scouting never submits; offer `/anfani-desk:submit` for final sheets.
