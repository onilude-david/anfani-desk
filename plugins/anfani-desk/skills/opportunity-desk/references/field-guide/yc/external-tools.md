# External tools for the YC application

Researched October 2026. Deadlines, rules and policies change: check each programme's own page before acting.

What other people have built to help founders get into Y Combinator, what each is worth, and what this skill borrows.
Read 2026-10-17. Nothing here is bundled with this plugin. Licences checked through the GitHub API; where the API and the
README disagree, the stricter reading wins.

Licence rule for this file: only MIT, Apache-2.0, BSD and CC-BY material is adapted, always in our own words and always
credited. Material without a licence file is listed for awareness and not adapted. YC's own pages and Paul Graham's
essays are copyrighted; they are summarised and cited, never copied.

## 1. Candidates

| # | Name and URL | Licence | What it does | Quality | Worth borrowing |
|---|---|---|---|---|---|
| 1 | apply-yc (thisisfatih) https://github.com/thisisfatih/apply-yc | MIT | Claude Code plugin: drafts and critiques a YC application, form-fill helper, founder profile, interview prep, reapplying notes, evals on three public applications | Useful (best overall) | Question-by-question critique order; compression levels per answer (notes / dense / plain); "TL;DR first sentence" and "stand-alone answer" checks; interview prep list; reapplication delta check; sources file with refresh schedule |
| 2 | yc-application-review (frenchie4111) https://github.com/frenchie4111/yc-application-review | MIT | Claude Code skill: partner-style triage of `YC_APPLICATION.md`; partner, coach and loop modes; JSON output; reviews in a fresh sub-agent so the chat's bias does not leak in | Useful | INTERVIEW / BORDERLINE / ARCHIVE verdict; top 3 fixes plus "the one question"; per-question "tests / 10 out of 10 / anti-patterns / forcing question"; loop mode that asks for facts, never invents them, stops at 3 rounds; fresh-context review; eight-label rubric (clarity, specificity, demand, founder fit, traction, why now, scope, market) |
| 3 | yc-partner (morajabi) https://github.com/morajabi/yc-partner | MIT (code and guides; the bundled corpus of YC transcripts, essays and tweets is third-party and not MIT) | Source-grounded knowledge pack: application review, hygiene pass, interview prep, office hours; 418 captured sources with line citations; eval fixtures | Useful (deepest sourcing) | Six review passes (comprehension, evidence, question, source, risk, calibration); "claim discipline" (find the strongest true claim, make it falsifiable); hygiene checklist; "do not down-rank for being early"; solo-founder handling; inverted-pyramid interview answers; founder-dynamics questions |
| 4 | gstack office-hours (Garry Tan) https://github.com/garrytan/gstack (office-hours/) | MIT | Office-hours mode inside Garry Tan's Claude Code toolkit: six forcing questions, push-twice posture, anti-sycophancy rules, routing by stage | Useful | Six forcing questions (demand reality, status quo, the named human, narrowest wedge, observed surprise, future fit); stage routing; banned soft phrases for the reviewer; "take a position and say what evidence would change it" |
| 5 | yc-application-superpower (Dedsec-Xu) https://github.com/Dedsec-Xu/yc-application-superpower | MIT | Claude Code skill: reads the live form, interviews the founder for facts, lints AI voice, fills the form, never submits | Useful | Fact interview in batches of 3 to 4 with chased follow-ups; `[NEEDS FOUNDER INPUT]` placeholder rule (matches our `[TBC]`); "could a stranger write this from the landing page?" test; housekeeping questions (entity, equity, SAFEs, other accelerators); three questions to answer before drafting |
| 6 | roast-yc-application (DominikScholz) https://github.com/DominikScholz/roast-yc-application | MIT | Scores an application 0 to 100 across eight weighted categories | Thin but usable | Weighted categories (clarity 20, founders 20, problem 15, traction 15, market 10, team 10, video 5, x-factor 5); traction ladder from revenue down to nothing |
| 7 | yc-roaster-application-coach (gjarrosson / Lobster Capital) https://github.com/gjarrosson/yc-roaster-application-coach | README says MIT; no LICENSE file in the repo and GitHub reports none | Coaching skill plus MCP server; per-question guidance files; common mistakes list | Useful, licence unclear | Read for awareness only. Its mistakes list (belief without evidence, top-down market size, vanity metrics, projections as traction, one anecdote as a pattern) overlaps sources 1 to 3, so nothing is lost by not adapting it. Ask the author to add a LICENSE before reuse |
| 8 | yc_interview (wkoszek) https://github.com/wkoszek/yc_interview | BSD-2-Clause | About 140 interview questions collected from the web | Useful (question bank) | Raw question bank, deduplicated and grouped in section 3 below |
| 9 | iPG (jamescun) https://github.com/jamescun/iPG | No licence | Browser page that fires random interview questions on a timer; written by founders for their own YC interview | Thin, historic (188 stars) | Idea only: random order, timer, one question at a time. Question text not reused |
| 10 | yc-interview-prep (plbiojout) https://github.com/plbiojout/yc-interview-prep | MIT | Voice mock interview built on OpenAI Realtime and Chainlit | Thin (needs an OpenAI key; little prompt content) | Nothing beyond the idea of voice practice; our Whisper kit already covers transcription |
| 11 | ycip (shauvik) https://github.com/shauvik/ycip | No licence | Python script that reads random questions aloud | Thin, 2017 | Nothing new |
| 12 | yc-office-hours (crealwork) https://github.com/crealwork/yc-office-hours | No licence | Office-hours skill with modes and verdicts (proceed, test first, pivot, kill) | Useful idea, not adaptable | Awareness only |
| 13 | yc-agents (vsevolodl) https://github.com/vsevolodl/yc-agents | MIT | 30 sub-agent prompts themed on Startup School, including an application coach | Thin (generic persona prompts) | Nothing that sources 1 to 5 do not do better |
| 14 | accelerator-application (shawnpang/startup-founder-skills) https://github.com/shawnpang/startup-founder-skills | MIT | Multi-accelerator skill with a directory of 40+ programmes | Thin for YC, useful for breadth | The accelerator directory, if the applicant later wants Techstars or 500 Global too |
| 15 | yc-advisor (agent37-platform) https://github.com/agent37-platform/agent37-skills-collection | MIT (wrapper; bundled YC library content is third-party) | Retrieval skill over 443 YC library resources | Useful for general startup questions, not for the form | Tiered retrieval pattern only |
| 16 | yc-startup-school (team-attention) https://github.com/team-attention/yc-startup-school | No licence | Transcript archive of 54 Startup School lectures | Reference only | Not adapted; link YC's own library instead |
| 17 | ycombinator-skills (jona) https://github.com/jona/ycombinator-skills | No licence | One skill per Startup School speaker | Thin | Nothing |
| 18 | investor-question-bank (josezuma) https://github.com/josezuma/investor-question-bank | MIT | Generator for 200+ partner-style questions | Thin (generated) | Nothing beyond source 8 |
| 19 | yc-ecosystem (LeadMagic gtm-skills) https://www.skills.sh/leadmagic/gtm-skills/yc-ecosystem | MIT | Broad YC ecosystem guide: free resources, application, Demo Day | Thin for the application | Nothing specific |
| 20 | YC official: How to Apply (Paul Graham) https://www.ycombinator.com/howtoapply | Copyright YC | The essay behind every tool above | Primary source | Summarised in section 2; not copied |
| 21 | YC official: Interview Guide https://www.ycombinator.com/interviews and founder video page https://www.ycombinator.com/video | Copyright YC | Interview format and video rules | Primary source | Summarised in sections 3 and 4 |
| 22 | Public accepted applications: Dropbox S07 https://www.ycombinator.com/apply/dropbox ; GitLab, Lago, Bedrock samples in source 2's `application-samples/` | Copyright of the founders | Real answers, used by sources 1 to 3 as calibration | Calibration only | Read, never copy. Third-party "reconstructed" applications (Round Funded, Flowjam) are commentary, not real forms |

Searched and found nothing YC-specific: anthropics/skills, ComposioHQ/awesome-claude-skills, travisvn/awesome-claude-skills.
VoltAgent/awesome-agent-skills lists only gstack office-hours. No public repo of real interview recordings exists; YC
keeps applications private, so Dropbox's (published by YC) is the one canonical full text.

## 2. Application review rubric (the one-minute skim)

Adapted from apply-yc (MIT), yc-application-review (MIT), yc-partner (MIT) and gstack office-hours (MIT), checked against
YC's How to Apply page. Rewritten in our words.

### How a partner reads

- Volume decides the method. YC's own page describes partners reading about a hundred applications a day, alone, and
  spending roughly twenty seconds on the idea before moving to the founders. More time goes only to founders who look
  promising (YC, How to Apply).
- The default is no. The application has to earn the interview in the first pass (apply-yc).
- Partners do not read in order and may open any answer cold. Every answer must stand alone (apply-yc).
- The reader needs to retell the company after one read: who the founders are, what exists today, whether anyone uses
  it, what is special. If they cannot, the application is weak no matter how good the business is (yc-partner).

### The first-sentence test (apply to every answer)

The first sentence of every answer must be the whole answer in miniature. Everything after it is evidence. If a partner
reads only first sentences, they should still have the application.

| Question | The first sentence must contain | Fails if it opens with |
|---|---|---|
| 50-character description | The user and the action, in words a twelve-year-old knows | A category word, "platform", "AI-powered", a cute analogy nobody can unpack |
| What does the company make | What the user does with the product today | Mission, vision, the market, the founders' feelings, the tech stack |
| How far along are you | A date and a number ("Live since March; 212 weekly users; 9 paying") | "We are in beta", "early traction" |
| Are people using it / how many | The count of active users, with your definition of active | Waitlist or sign-up totals presented as users |
| Revenue | The monthly figure and what it is for | Projections, gross transaction value dressed as revenue |
| Why this idea / domain expertise | The moment you met the problem, or the specific knowledge you hold | "We saw a large market" |
| Competitors and what you understand | The named rival you fear most, then the one thing you believe that they get wrong | "We have no competitors" or "better UX" |
| How you make money / how much | Price times buyers, bottom-up | A top-down market figure from a report |
| Most impressive thing (per founder) | One hard, specific, checkable achievement with its result | An adjective about the founder, or the startup itself |
| Hacked a non-computer system | The system and how you beat it | Something legal and conventional, or the startup |
| Project built together | The thing, the date, the link | "We met at university" with nothing shipped |
| Surprising or amusing discovery | The discovery itself, in one line | A humble-brag about the company |
| Reapplying: what changed | The delta since last time, as numbers | An empty field or "N/A" |

### Compression levels (apply-yc)

- Notes: the 50-character line, stage, time worked, stack. Fragments are fine. "Live March 2026. 9 paying. NGN 2.1m MRR."
- Dense: product, impressive thing, competitors, why this idea. First sentence stands alone; each sentence after earns
  its place.
- Plain: co-founder story, money, the hack, the amusing thing. Full sentences, no hedging ("we believe", "we feel").

### Scoring (weights from roast-yc-application, MIT; labels from yc-application-review, MIT)

Score each area, then give one verdict.

| Area | Weight | What earns full marks |
|---|---|---|
| Clarity | 20 | Idea clear from the first sentence; no jargon; the retelling test passes |
| Founders | 20 | Specific, hard, checkable achievements; proof of building, not credentials |
| Problem and insight | 15 | A named user with a painful workaround; one belief the incumbents get wrong |
| Traction and progress | 15 | Real usage with a denominator; retention; dated progress |
| Market and money | 10 | Bottom-up sizing; named competitors including the status quo |
| Team | 10 | Who writes the code; time worked together; everyone full-time or a plan |
| Video | 5 | Under a minute; all founders; talking, not a demo or an ad |
| The extra | 5 | A hack, a surprise, a detail only these founders could know |

Traction ladder, strongest first (roast-yc-application): profitable revenue, revenue, paying users, active free users,
sign-ups, letters of intent, user interviews, nothing.

Verdict (yc-application-review): INTERVIEW, BORDERLINE or ARCHIVE, with one sentence why. Then exactly three fixes that
would move the verdict most, then the single hardest question the draft has not answered.

### Review passes (yc-partner, MIT)

1. Comprehension: state in four lines what it is, who the first user is, what exists now, what the application claims.
2. Evidence: list product, user, revenue, growth, retention, founder fit, technical ability. Mark what is missing.
3. Question: check every answer against its actual prompt. A strong answer elsewhere does not excuse a dodged one.
4. Claim discipline: find the strongest true claim and make it falsifiable. If a bigger claim needs missing evidence,
   ask for the evidence; never write the claim.
5. Risk: misleading numbers, who owns the code, founder dynamics, the incumbent problem.
6. Calibration: no score that the text and sources do not support. Name the uncertainty.
7. Hygiene last: required fields, typos, links, video attached, demo link and login if needed.

### Review conduct

- Review in a fresh context. A reviewer that helped write the draft is biased (yc-application-review). In the desk,
  run the review in a sub-agent that sees only the rubric and the draft.
- Loop for facts, not wording. Turn each critique into one factual question (a name, a number, a date). Skipped
  questions leave the answer weak and unchanged. Stop after three rounds: after that the business is the bottleneck,
  not the prose (yc-application-review).
- Take a position on every answer and say what evidence would change it (gstack office-hours).
- Do not mark an application down for being early. YC says many funded companies are only an idea at application
  (yc-partner, citing the YC FAQ). Look harder at the founders and their speed instead.
- Solo founders are not told to stay away. YC funds them; flag the risk and move on (yc-partner).

## 3. Mock-interview protocol (10 minutes, rapid fire)

Adapted from apply-yc (MIT), yc-partner (MIT), gstack office-hours (MIT) and yc_interview (BSD-2-Clause), checked
against YC's Interview Guide. Rewritten in our words.

### The real thing

- Ten minutes on video, all founders on camera, usually two or three partners with the application open. No slides.
  Random access, not a pitch: questions jump around (YC Interview Guide; Paul Graham via yc-partner).
- YC warns that heavy rehearsal backfires. The best preparation is new progress since applying (apply-yc, quoting the
  guide). So the mock runs once or twice, not eight times.
- Key numbers may sit on paper beside the laptop (YC Interview Guide).

### Setup (5 minutes before)

1. The examiner reads the application and the founder's numbers sheet. It marks the three weakest answers; those are
   where the interview will go.
2. Multi-founder teams decide who takes product and technical questions and who takes business ones (yc-partner).
3. Demo loaded in a tab. Numbers sheet open: users, active definition, revenue, growth, retention, burn, runway.

### Running it

- Clock: 10 minutes hard stop. The examiner announces 5 minutes and 1 minute left.
- Opener, always: "What are you working on?" Target 30 seconds, plain words, one example.
- Then 18 to 25 questions. Pace about 25 seconds per answer. The answer is the first sentence; context only if time is
  left (inverted pyramid, yc-partner citing Garry Tan).
- Interrupt when: an answer passes about 30 seconds; the first sentence does not answer the question; an adjective
  stands where a number should be; a waitlist is called users; the founder recites a prepared line that does not fit.
- Follow-up ladder (gstack office-hours): ask, then push once ("how many, exactly?"), then push again ("name one").
  The first answer is the polished one; the real one comes on the second or third push.
- Pressure moves: state something wrong about the business and see if the founder corrects it politely (apply-yc);
  "someone pitched this an hour ago, what else have you got?" (yc_interview); "what if we don't fund you?"
- Route by stage (gstack office-hours): no product yet, stay on demand, status quo and the named user; users but no
  revenue, stay on status quo, wedge and observed surprise; paying customers, stay on wedge, surprise and future fit.
- Share the floor: each founder must take at least one question. If one founder dominates, steer to the other.

### Question bank (grouped from yc_interview, BSD-2-Clause, and the sources above; paraphrased)

- What it is: What are you working on? Show me. Where is the hard part? What is new here?
- Users and demand: Who needs this most, by name? What did they do yesterday without you? Who would be upset if you
  vanished tomorrow? What has surprised you about how people use it? Why do the reluctant ones hold back?
- Traction: How many users, how many active, how do you define active? How many pay, and how much? Week-on-week growth?
  Where do new users come from? How many did you already know? What have you shipped since you applied?
- Market and money: How do you make money? Price times buyers, out loud. How big can this get, and what sequence of
  markets gets you there? What is your burn and runway?
- Competition: Who do you fear most? Why has the incumbent not done this? What do you know that they do not? What
  happens if the biggest company in the space copies you?
- Founders: How did you meet, and what have you built together? Who writes the code? Is everyone full-time? Who is the
  boss? What system have you beaten? What is the biggest mistake you have made?
- Risk and resolve: What is the biggest risk? What will be your biggest problem in six months? What will you do if we
  say no? (Expected answer: keep building.)

### Scoring the mock

After the clock stops, score each answer on three marks: first sentence answered the question (yes/no); a number or a
name was given (yes/no); under 30 seconds (yes/no). Then list:
1. The three answers that needed the most pushes.
2. Any claim the founder could not back with a number.
3. Any moment the founder was defensive. Calm candour about a weakness beats dismissing it (yc-partner, citing Jessica
   Livingston; YC Interview Guide).
4. One action before the real interview, and it should be progress (a customer, a launch), not more rehearsal.

## 4. Red-flag checklist

Adapted from apply-yc (MIT), yc-application-review (MIT), yc-partner (MIT), gstack office-hours (MIT),
roast-yc-application (MIT) and yc-application-superpower (MIT); checked against YC's How to Apply and video pages.

### Clarity

- [ ] The 50-character line uses a category word or an analogy a stranger cannot unpack.
- [ ] The product answer opens with mission, vision or the market, not what the user does.
- [ ] Insider jargon instead of the industry's own words.
- [ ] Any sentence a stranger could write after two minutes on the landing page (yc-application-superpower).
- [ ] Hedging: "we believe", "we think", "we feel", "we hope".
- [ ] Stock AI phrasing or sales words; run the desk's banned-word list and the humanizer pass.

### Evidence

- [ ] Waitlist, sign-ups or likes presented as users.
- [ ] Numbers without a denominator or a definition of active.
- [ ] Projections offered as traction.
- [ ] One enthusiastic customer or one big-company conversation offered as a pattern.
- [ ] Gross transaction value labelled as revenue.
- [ ] No named user anywhere in the application.
- [ ] Everything in the future tense; nothing shipped recently.
- [ ] Any number the founder cannot reproduce on the spot in an interview. Inflated or misleading claims are
      disqualifying (yc-partner, citing YC's Startup School talk).

### Market and competition

- [ ] "No competitors", or competitors named without the status quo workaround.
- [ ] The edge is "better UX" or "we will execute better". YC's page says plainly that execution is not an insight.
- [ ] A top-down market figure with no bottom-up maths.
- [ ] A recent YC company in the same space goes unmentioned (yc-application-superpower).
- [ ] A known tarpit with no answer to why it is different: consumer social, a marketplace with no supply plan, a thin
      AI wrapper with no distribution (yc-application-review).

### Founders and team

- [ ] The impressive-thing answer is an adjective, a job title or the startup itself.
- [ ] Credentials without proof of building.
- [ ] Unclear who writes the code, or code written by people outside the founding team.
- [ ] Part-time founders with no plan or date to go full-time.
- [ ] Co-founders with nothing built together and no admission of the gap.
- [ ] A known weakness hidden instead of named. YC's page asks applicants to disclose flaws partners will spot anyway.

### Hygiene

- [ ] Any required field empty; missing links or bios.
- [ ] Typos and grammar slips.
- [ ] Founder video over a minute, scripted, missing a founder, or a product demo instead of founders talking.
- [ ] No demo or product link when one exists; login needed but not given.
- [ ] Reapplying and the "what changed" field is empty.
- [ ] Location, entity, equity, SAFEs or other accelerators answered inconsistently, or the "how did you hear about
      YC" answer invented. It is checkable (yc-application-superpower).

### Interview

- [ ] Answers sound memorised or start before the question ends.
- [ ] Talking over partners or over a co-founder; co-founders contradict each other.
- [ ] Defensive under pushback, or folding when a partner is wrong.
- [ ] Demo not loaded.
- [ ] A visible risk waved away.

## 5. Notes for this skill

- Our existing rules already cover several borrowed ideas: `[TBC]` for anything only the founders know (same as the
  superpower skill's founder-input placeholder), facts only from `desk/profile.md`, no invented details, and the
  founders submit. Keep those; they are stricter than any tool above.
- YC's current AI-use policy for the form was not confirmed in this research; check the live form and record it on the
  answer sheet, as the desk does for every programme. Either way, the interview exposes any answer the
  founder cannot defend in their own words.
- Do not paste sample answers from Dropbox, GitLab or any accepted application into a draft. Use them only to calibrate
  length and directness.

## Sources (read 2026-10-17)

- thisisfatih, apply-yc, MIT: https://github.com/thisisfatih/apply-yc (critique-rubric.md, interview-prep.md,
  application-questions.md, successful-applications.md, docs/sources.md)
- frenchie4111, yc-application-review, MIT: https://github.com/frenchie4111/yc-application-review (skills/yc-review/SKILL.md)
- Mo Rajabi, yc-partner, MIT: https://github.com/morajabi/yc-partner (guides/application-review.md, interview-prep.md,
  application-hygiene.md, README.md)
- Garry Tan, gstack office-hours, MIT: https://github.com/garrytan/gstack/tree/main/office-hours
  (sections/phase-2a-startup-diagnostic.md)
- Dedsec-Xu, yc-application-superpower, MIT: https://github.com/Dedsec-Xu/yc-application-superpower
  (references/interview.md, references/writing-guide.md)
- Dominik Scholz, roast-yc-application, MIT: https://github.com/DominikScholz/roast-yc-application (references/scoring-rubric.md)
- Wojciech Koszek, yc_interview, BSD-2-Clause: https://github.com/wkoszek/yc_interview
- Lobster Capital, yc-roaster-application-coach (licence unclear, not adapted): https://github.com/gjarrosson/yc-roaster-application-coach
- James Cunningham and Colin Hayhurst, iPG (no licence, not adapted): https://github.com/jamescun/iPG
- plbiojout, yc-interview-prep, MIT: https://github.com/plbiojout/yc-interview-prep
- crealwork, yc-office-hours (no licence, not adapted): https://github.com/crealwork/yc-office-hours
- vsevolodl, yc-agents, MIT: https://github.com/vsevolodl/yc-agents
- shawnpang, startup-founder-skills, MIT: https://github.com/shawnpang/startup-founder-skills
- agent37-platform, yc-advisor, MIT: https://github.com/agent37-platform/agent37-skills-collection
- LeadMagic, yc-ecosystem, MIT: https://www.skills.sh/leadmagic/gtm-skills/yc-ecosystem
- Y Combinator, How to Apply (Paul Graham): https://www.ycombinator.com/howtoapply
- Y Combinator, Interview Guide: https://www.ycombinator.com/interviews
- Y Combinator, founder video guidance: https://www.ycombinator.com/video
- Y Combinator, Dropbox S07 application: https://www.ycombinator.com/apply/dropbox
- Y Combinator, FAQ: https://www.ycombinator.com/faq
