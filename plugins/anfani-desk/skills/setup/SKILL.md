---
name: setup
description: Set up Anfani Desk for a new user - interview them, read their CV and links, and create their private desk/ folder (profile, gates, priorities, voice, story bank, pipeline). Run once before scouting or filling; run again to update.
argument-hint: "[path to CV or folder of documents]"
---

# Set up Anfani Desk

You are setting up a private opportunity desk for the person you are talking to. Everything you write goes into a
`desk/` folder in their current project. Nothing leaves their machine. Be warm, quick and plain.

## Steps

1. **Explain in three lines** what the desk does (finds opportunities that fit them, fills applications from their real
   record, submits only when they say yes to the final form) and that their data stays in `desk/` on their computer.

2. **Create the folder.** If `desk/` exists, read it and offer to update rather than overwrite. Otherwise copy every file
   from `${CLAUDE_PLUGIN_ROOT}/skills/opportunity-desk/templates/` into `desk/` (except `answer-sheet.md`), and create
   `desk/applications/`. Add `desk/` to `.gitignore` if the project is a git repo and the user does not want their
   record committed (ask once).

3. **Read what they give you.** If they passed a path ($ARGUMENTS) or attach a CV, read it: CV, LinkedIn export,
   personal site, past applications, award letters. Extract facts into `desk/profile.md` with the source of each.
   Ask before reading anything outside the project folder. Never copy passport, ID or bank numbers; record the file
   name only.

4. **Interview (about 15 questions, a few at a time).** Ask only what the documents did not answer:
   - Nationality (every citizenship), country of residence, date of birth.
   - Highest degree, institution, year, class or GPA, language of instruction; any English test.
   - Current roles and organisations; for each organisation they run: what it is in their own words, registration,
     size, users or reach with a date.
   - Goals, ranked: talent visa, master's, funded events, awards, fellowships, recognition, speaking, grants, startup
     programmes, jobs. What is out of scope.
   - Deal-breakers: fees, relocation, travel, time per week.
   - Visas they hold or have been refused (for travel-based programmes).
   - Two or three things they wrote themselves (for their voice), and how they introduce themselves in one sentence.
   - Three true moments from their work they are proud of (for the story bank).
   - Referees who would say yes.
   Write each answer into the right file as you go: `profile.md`, `gates.md`, `priorities.md`, `voice.md`,
   `story-bank.md`, `evidence.md`.

5. **Build the age clock** in `desk/calendar.md` from their date of birth: the dates they pass 25, 27, 30 and 35, and
   which common programme limits those dates close.

6. **Read back** a ten-line summary of their profile, gates and priorities. Fix anything they correct.

7. **Finish** with what to do next:
   - "Scout for me" or `/anfani-desk:scout` to find opportunities that fit.
   - `/anfani-desk:fill <link>` to fill a specific application.
   - `/anfani-desk:submit <folder>` when a sheet is final: the desk fills the form in your browser, shows you every
     field, and submits only on your yes.
   - Write answers, outcomes and instructions in `desk/inbox.md` any time; the desk reads it on every run.
   - Optional: connect Gmail in Claude to let the desk scan your inbox for calls and invitations.

Never invent a fact to fill a field. Unknown means `[TBC]`.
