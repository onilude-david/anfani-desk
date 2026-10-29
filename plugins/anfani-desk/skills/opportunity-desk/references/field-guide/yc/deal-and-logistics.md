# YC deal and logistics for Nigerian founders

Researched October 2026. Deadlines, rules and policies change: check each programme's own page before acting.

Research of 17 October 2026. Sources at the end. This is research, not legal, tax or immigration advice; YC
introduces accepted founders to lawyers and immigration attorneys, and every step below gets confirmed with them.
Most of it applies to any non-US team; the visa and Nigerian-company sections are written for Nigerian applicants.

---

## 1. The standard deal (from YC's deal page, read 17 October 2026)

- **$500,000 per company**, committed on the day of acceptance, not tied to milestones. YC does not wait for the
  batch to start. No fees.
- **Two SAFEs signed at the same time, plus a YC Agreement:**
  - **$125,000 on a post-money SAFE for 7%** of the company. In the first priced round it converts into 7%,
    measured after all SAFEs and convertibles convert and including any existing option pool.
  - **$375,000 on an uncapped SAFE with a Most Favored Nation (MFN) clause.** It converts on the terms of the
    lowest-cap SAFE (or better terms, such as a discount) the company issues between the MFN start date (around
    the start of the batch) and the priced round. YC's example: if the next SAFEs carry a $15M post-money cap,
    the MFN SAFE converts into $375,000 ÷ $15M = 2.5%.
  - **The YC Agreement** sets YC-specific guidelines and rights, including a right to participate in future
    rounds (pro rata).
- **Order at the priced round:** SAFEs convert to preferred; the option pool is created or topped up to the
  agreed size; new money comes in. The round and the pool dilute YC.
- **No "gotcha" terms**, YC says (for example, no enhanced returns in downside exits).
- **Partner credits:** the apply page lists $12M+ in credits and deals (OpenAI, Anthropic, AWS, Google Cloud,
  Azure, Stripe and others).
- **What the money is for:** YC's FAQ says usually founder salaries first, so founders can work full time; it may
  also cover travel to San Francisco.
- **How to judge it:** YC's FAQ points to Paul Graham's equity equation: take the deal if YC raises your expected
  outcome by more than about 7.5%.
- **Worked example for planning (not a forecast):** if the next round after YC is a SAFE at a $10M post-money
  cap, YC would end near 7% + 3.75% = 10.75% before the priced round. A lower next cap means more for YC.
  Founders should model this before raising after Demo Day.
- **The SAFE itself:** YC publishes the post-money SAFE forms and a free "Send a SAFE" tool at
  ycombinator.com/documents. The SAFE converts automatically at a priced round.

African reaction when the $500k deal launched (TechCabal, January 2022): some local investors worried the
uncapped MFN would make it harder for emerging-market founders to close the next round if their next cheques are
small. Model the MFN against realistic Nigerian seed caps.

---

## 2. Entity: what YC requires and how a Nigerian company gets there

**YC's rule.** YC invests in US (normally Delaware), Canadian, Cayman and Singapore corporations. You do not need
to incorporate before applying. If accepted and already incorporated elsewhere, you create a parent in one of
those four; the existing company usually becomes its subsidiary and keeps operating at home; IP can sit with the
parent or the subsidiary. YC introduces lawyers, but the FAQ warns the process takes significant effort from the
founders. (Deal page; FAQ)

**A product held inside an existing company.** A common case: the startup's product sits inside a company the
founders already run (for example a services agency with client revenue and staff). Two routes, for the lawyers to
choose between:

| Route | What happens | For | Against |
|---|---|---|---|
| A. New US company takes the product | Form a Delaware C-corp. The existing company assigns or sells the product's code, brand, domains, app listings and user data to it under a written agreement. If the product needs a Nigerian operating company, the Delaware company forms a new Nigerian subsidiary. The existing company stays a separate services firm. | Keeps the agency out of the YC company. Cheap to form (Stripe Atlas about $500). Clean cap table. | The IP transfer is a disposal by the existing company: price it at market value and check Nigerian tax on any gain `[TBC: the company's turnover; the small-company exemption]`. Staff who wrote the product's code were that company's employees; their IP must be confirmed as the company's first. YC and its lawyers must accept the structure. |
| B. Flip the existing company | Founders and other shareholders swap their shares for shares in a Delaware parent; the existing company becomes its subsidiary. | YC's standard path for companies already incorporated abroad. | The services business, its staff, contracts and liabilities come inside the YC company. Expensive: lawyer-led flips are quoted at about $30,000–120,000 (Causo, citing typical Orrick, Wilson Sonsini and Cooley ranges). Nigerian tax and regulatory steps on a share transfer to a foreign parent. |

The desk's reading: route A usually fits better, because YC asks applicants to break out consulting income from
product income and does not want an agency inside a startup. Confirm with YC's lawyers after acceptance; do nothing
before then except gather the facts below.

**Facts to have ready** `[TBC from the founders]`: the existing company's shareholders and percentages; whether
any other person holds its shares; who wrote which parts of the product and under what contract; whether the
company has employment contracts with IP clauses; where the product's user data is held; the company's latest
annual turnover (for the tax tests); any grants or agreements naming the company as the product's owner.

**Nigerian side (if a Nigerian subsidiary is owned by the Delaware parent, or an existing Nigerian company is flipped):**
- **NIPC.** Companies with foreign participation register with the Nigerian Investment Promotion Commission after
  CAC incorporation (NIPC guidelines). Vendor guides add a business permit and a ₦100 million minimum share
  capital for foreign-owned companies; this is from vendor guides only and must be checked with counsel.
- **CAC filings for a share transfer:** board resolution, share transfer instrument, stamp duty paid to the tax
  authority, updated register of members (vendor guide; confirm).
- **Certificate of Capital Importation (CCI).** When the US parent sends YC money into Nigeria, the receiving bank
  issues an electronic CCI. It is optional, but it is what gives access to official FX for repatriating
  dividends or capital later, and the CBN asks for it on divestment. Apply at the time the money comes in.
  (Mondaq; TheCable)
- **Capital gains tax (Nigeria Tax Act 2025, in force 1 January 2026).** Company gains are now taxed at the
  company income tax rate, up to 30% (was 10%). Individuals' gains join their income, taxed up to 25%. A new
  rule (section 46) treats shares in a foreign company as Nigerian if more than half their value in the prior
  365 days comes from Nigerian assets, so selling Delaware shares can be taxed in Nigeria if the value is
  Nigerian. A share disposal exemption applies below ₦150m proceeds and ₦10m gains in 12 months. Small
  companies are exempt from company income tax. This affects later exits more than formation, but the flip
  itself and any IP sale need tax advice. (TechCabal, February 2026; Legal500)
- **Nigeria Startup Act 2022.** Offers some incentives to labelled startups (TechCabal mention); check whether a
  labelled Nigerian subsidiary keeps them `[TBC]`.

**US side (for the Delaware company):**
- **Formation:** Stripe Atlas (about $500, includes registered agent for a year, EIN application and founder stock
  paperwork) is the common route for foreign founders; Clerky for later financing paperwork. YC helps accepted
  companies incorporate. (Turing VC; Zecca Ross)
- **EIN:** without a US social security number, 15–25 business days via Atlas, longer by mail. Banking (Mercury
  is the usual first bank for Atlas companies) and EIN are the bottlenecks; plan 2–4 weeks on the Atlas and
  Mercury path, 45–90 days otherwise. (Turing VC)
- **83(b) election within 30 days** of issuing founder stock subject to vesting. Missing it causes tax on each
  vesting tranche. (Turing VC; Zecca Ross)
- **Form 5472 with Form 1120 every year** when a foreign person owns 25% or more. The penalty is $25,000 per form
  per year. Hire a startup tax firm from year one. (Turing VC)
- **Section 351:** a properly structured share exchange can be tax-deferred in the US if the transferring owners
  keep at least 80% control; home-country tax may still apply. (Zecca Ross)

**Timing.** YC's money arrives after the US company exists, has a bank account and signs the SAFEs. Start the
EIN and bank on the day of acceptance (about 11 December). The Nigerian steps can follow during the batch.

---

## 3. The batch: dates and what being there means

- **W27:** January to March 2027 in San Francisco, at YC's campus, starting with a three-day in-person kick-off.
  Weekly meetups in San Francisco through the batch. (Apply page; FAQ) Exact start date `[TBC: in the acceptance
  email]`.
- **In person is the rule.** YC ran remotely during Covid but has been in person since 2022 and says it works much
  better that way. After the three months, founders can live anywhere. (FAQ) A YC spokesperson told TechCrunch in
  2024 that YC requires all YC startups to move to San Francisco for the batch.
- **Time cost:** YC says a few hours a week if you attend everything recommended; all parts are optional, and the
  point is three months of focus. (FAQ)
- **Demo Day:** to an invite-only audience of about 1,000 to 1,500 investors and media, in person in San Francisco.
  W26's was Tuesday 24 March 2026; F26's is Wednesday 2 December 2026. W27's date is not yet published; late March
  2027 is the expected pattern (inferred). (Demo Day page and FAQ; YC 2026 Demo Day dates)
- **Launch YC and the Startup Directory:** companies launch publicly during the batch. (Demo Day FAQ)

---

## 4. Visas for Nigerian founders

### 4.1 The rule that changed everything: Proclamation 10998

- Signed 16 December 2025; effective 12:01 a.m. EST, 1 January 2026. Nigeria is on the **partial** list.
- **Suspended for Nigerian nationals:** entry as immigrants, and as non-immigrants on **B-1, B-2, B-1/B-2**, F, M
  and J visas. For any other non-immigrant visa, consular officers must reduce validity as far as the law allows.
  (Proclamation text; US Mission Nigeria)
- **Who it does not apply to:** people who were inside the US on 1 January 2026, or who held a valid visa on that
  date. Visas issued before 1 January 2026 were not revoked. Also exempt: US permanent residents; **dual nationals
  travelling on the passport of a non-designated country**; diplomatic and similar categories. (Proclamation
  section 6; US Mission Nigeria)
- **Case-by-case national interest exceptions** exist (Secretary of State or Homeland Security, or Attorney
  General). On 28 January 2026 the State Department delegated the State decision to the Assistant Secretary for
  Consular Affairs. There is no separate form: apply for the visa and present at the interview the facts showing
  why your travel serves a US national interest. (Proclamation; NAFSA; AILA notice) No public example of a startup
  founder getting one was found.
- **Applying is still allowed.** The Mission says those subject to the proclamation may apply and attend
  interviews but may be found ineligible; the $185 fee is not refunded. (US Mission Nigeria; TravelReady)
- **Status:** reviewed every 180 days. The US Mission said on 30 March 2026 that restrictions are not permanent
  and depend on Nigeria's screening and identity standards. No change for Nigeria was found as of October 2026.
  (ICIR; Visaverge; JQK Law)
- **It is by nationality, not by place.** A Nigerian citizen applying in London (or anywhere else) is subject to
  the same suspension. The Embassy states the visa bond requirement for Nigerian nationals applies regardless of place of
  application.

### 4.2 Other B-1/B-2 rules that apply on top

- **Visa bond:** Nigerian nationals found otherwise eligible for a B-1/B-2 must post a bond of up to $20,000
  before issuance, refundable if the conditions are kept. The State Department made the bond programme permanent
  on 3 August 2026 ($10,000, $15,000 or $20,000). Pay only when told by the officer, on the site named.
  (US Mission Nigeria; American Bazaar)
- **Validity:** since 8 July 2025 most non-immigrant visas for Nigerians are single entry, three months.
  (US Embassy, reciprocity notice) Single entry means leaving during the batch ends the visa.
- **Where to apply:** since September 2025, apply in your country of nationality or residence. For a founder living
  in Nigeria, that is Lagos; since 1 August 2026 routine visa services in Nigeria run only at the Consulate General
  in Lagos (Abuja stopped). A Nigerian founder resident in the UK applies in London. (Harvard HIO; US Mission Nigeria; TravelReady)
- **No interview waiver** in Nigeria at present; plan an in-person interview. The appointment service says its
  call centre cannot offer earlier dates. (TravelReady, citing the official service)
- **221(g) administrative processing:** cases can be held for extra checks with no fixed timeline; the post
  contacts you when done. (TravelReady, citing the official service) With a batch starting in early January, a
  221(g) hold alone can cost the batch.
- **Fees:** $185 MRV fee; a $250 visa integrity fee was enacted in July 2025 (Public Law 119-21) but was not yet
  listed on the Nigeria page in October 2026 `[TBC at booking]`. (TravelReady)
- **Social media:** applicants for several categories must set social accounts to public; check the current list
  before applying. (US Mission Nigeria visas page)
- **Wait times:** check the State Department's Global Visa Wait Times tool for each post on the day; third-
  party figures (for example about 82 days for London B1/B2) were undated and unverified.
- **What B-1 allows:** meetings, investor pitches, conferences and accelerator participation; not productive work
  or a US salary. ESTA entries cannot be extended or changed. (Passright; Startup.pk; Ardina Law)

### 4.3 The routes, ranked

1. **A valid US visa issued before 1 January 2026.** If a founder holds one, the proclamation does not apply
   to that founder `[TBC: does each founder hold any unexpired US visa?]`. Ask every founder first; this may
   settle it.
2. **A second citizenship.** A founder who also holds, for example, British citizenship travels on the British
   passport, falls under the dual-national exception, and would normally use ESTA rather than a visa `[TBC: their
   status; check ESTA eligibility]`. A UK visa or settled status alone does not change nationality.
3. **O-1A (extraordinary ability) work visa.** Not suspended for Nigerian nationals; validity may be reduced.
   NAFSA confirms O-1 and H-1B are outside the partial ban. Needs a US petitioner (the new Delaware company can
   petition), evidence across several criteria (awards, press, selective memberships, high pay, critical roles,
   expert letters), USCIS approval, then a consular interview (Lagos, or the post where the founder resides). Premium processing: $2,965,
   decision in 15 business days (RFEs restart the clock); plus the base petition fee `[TBC: current USCIS
   schedule]` and a $205 consular fee. USCIS's 2026 "hold" on applications from nationals of travel-ban countries
   was vacated by a federal court on 5 June 2026, and a class injunction on 24 August 2026 ordered processing to
   resume; the government is appealing. (NAFSA; Beyond Border; Startup.pk; JQK Law; court coverage) A founder with
   awards, press and selective roles may have a case; YC acceptance is often cited as supporting evidence. Timing is tight: acceptance about 11 December, petition, 15 business
   days, then a Lagos appointment. Realistic arrival is late January or February, not the kick-off.
4. **National interest exception at a B-1 interview.** Apply, attend, and present the YC acceptance and a lawyer's
   letter on why the travel serves a US interest. Outcome unknown; treat as a long shot.
5. **Remote participation for part of the batch.** YC's stated rule is in person. YC told TechCrunch in 2023 that
   founders of GigaML did office hours over Zoom after two visa denials. A single outlet reported YC considering a
   remote exception for Ukrainian founders for W26; unverified. Ask YC directly on acceptance; do not assume it.

**What YC provides.** YC works with immigration attorneys who have helped hundreds of founders; an accepted
company is connected with an attorney who builds an individual immigration plan. YC does not issue visas. Its
acceptance letter and investment documents are the evidence of purpose; nothing found shows YC issues a formal
"invitation letter" beyond that `[TBC: ask YC's attorney]`. (FAQ)

**Expedite options.** None reliable in Lagos: the official service says the call centre cannot offer earlier
dates. A 2016 Nigerian team got an expedited interview only through an investor's contacts, with days to spare
(TechCabal). Check the appointment system for an emergency or expedited request route on the day of acceptance.

**Plan of action (start now, before the application):**
1. Today: every founder checks passport validity and any existing US visas; any founder living abroad confirms
   their nationality and residence status.
2. Before the application deadline: decide how to answer the location question honestly (see `application.md` Q13–14). Do not
   promise attendance that depends on a suspended visa without saying so.
3. If invited to interview: prepare a two-sentence answer on the visa plan.
4. On acceptance: ask YC for the immigration attorney the same day; start the O-1 evidence file for the founder
   whose record is stronger; book visa appointments at every relevant post at once.

---

## 5. Full-time and other companies

- YC FAQ: you can apply while a full-time student or employee, but founders commit to work full time on the
  company during the batch and afterwards if accepted.
- Partners treat leaving other work as evidence of seriousness (Caldwell, 2023) and question part-time co-founders
  in interviews (Gyfted, 2025).
- The form asks founders to separate consulting income from product income (revenue source question), and to list
  entities set up to employ developers or other service providers. Any existing company the founders run must be
  disclosed, and its income kept apart from the startup's.
- Michael Seibel (YC Library): investors avoid startups whose product was built by an outside dev shop. If the
  product was built by the founders' own firm, say so plainly, and move the IP so the startup owns it.
- Answer pattern and wording: `application.md` section 3.

---

## 6. YC-backed African companies (from YC's directory data)

Pulled from the open YC directory dataset (yc-oss, read 17 October 2026) by location; status as listed there.
Africa-wide count in the dataset: about 97 companies; about 53 tied to Nigeria. Press counts differ (49 to 60
Nigerian companies), depending on method.

**Nigeria, by batch**
- W16 Paystack (payments; acquired by Stripe)
- S16 Flutterwave (payments)
- S17 Releaf Earth (agri processing); Helium Health (health tech)
- W17 Tizeti (internet provider); Aella (credit); Reliance Health (health insurance); BuyPower (bill payments);
  Nomba, formerly Kudi (business banking and payments)
- S18 Kobo360 (freight marketplace; inactive); Helicarrier, formerly Buycoins (crypto); Cowrywise (savings and
  investing)
- W19 Thrive Agric (farm finance and markets); CredPal (buy now pay later); 54Gene (genomics; inactive);
  **Schoolable (tuition collection for private schools; education)**; Spring in Africa
- W20 Bamboo (brokerage); Termii (messaging); CrowdForce (agent network; acquired); Healthlane; SEND (freight
  forwarding)
- W21 Sendbox (fulfilment); Mono (open banking; acquired); **Vendease (marketplace for restaurant supplies)**; Flux
- S21 Infiuss Health (two-sided marketplace for medical research); Payhippo (SME loans); Suplias (FMCG inventory
  credit); Mecho Autotech (auto repair)
- W22 (Nigeria's peak: 18 of 24 African startups) Remedial Health (pharmacy B2B marketplace); Touch and Pay;
  **Heyfood (food delivery marketplace)**; Plumter; Eazipay (payroll); Prembly (identity); **Grey (accounts for
  remote workers)**; Dojah (identity); Convoy; **Vendy (marketplace on WhatsApp)**; Sendme (inactive); Simplifyd;
  Rank; Duplo; Topship (logistics)
- S22 Bridgecard (inactive); **Chowdeck (food delivery marketplace)**; Anchor (embedded finance); FoodCourt; Pivo
  (inactive)
- W23 **Shekel Mobility (B2B marketplace for auto dealers)**; Waza (B2B payments)
- S23 Chow Central (food)

**Rest of Africa, education, jobs and talent, marketplaces**
- W12 Wave (Senegal, mobile money)
- W17 WaystoCap (Morocco, B2B trade marketplace; acquired)
- S20 MarketForce (Kenya, merchant app)
- W20 **Workpay (Kenya, payroll and employer-of-record)**
- W21 **Kidato (Kenya, online K-12 school; education)**
- W22 **Skillza (Egypt/UAE, tools for teachers and schools; inactive)**; Tendo (Ghana, social selling)
- S21 **Fingo Africa (Kenya, neobank for youth; acquired)**
- S23 Eden Care (Kenya, health claims); VaultPay (DRC)
- W24 Triply (Kenya, travel software)
- Sp26 RASPIRE (Egypt, security)

**What the list says.** Education (Schoolable, Kidato, Skillza), youth or worker finance (Fingo, Grey,
Workpay) and marketplaces appear, but none is a talent or opportunity-matching product. Fintech dominates (TechCrunch: over half of 92 African YC companies by 2024). African acceptances
dropped after YC returned to in-person batches (none in S24; three in each of the three batches before), which
YC links to the move-to-San-Francisco requirement. The bar is the same; the logistics are harder.

---

## Sources (opened and read 2026-10-17)

YC official
1. https://www.ycombinator.com/deal (Kirsty Nathoo, "The Y Combinator Deal")
2. https://www.ycombinator.com/apply
3. https://www.ycombinator.com/faq
4. https://www.ycombinator.com/documents (SAFE)
5. https://www.ycombinator.com/demoday
6. https://www.ycombinator.com/demoday/faq
7. https://www.ycombinator.com/blog/2026-demo-days
8. https://www.ycombinator.com/library/It-how-to-apply-and-succeed-at-yc (Dalton Caldwell, 2023)
9. https://www.ycombinator.com/library/7v-should-i-use-a-dev-shop (Michael Seibel)
10. https://paulgraham.com/equity.html

Immigration
11. https://www.whitehouse.gov/presidential-actions/2025/12/restricting-and-limiting-the-entry-of-foreign-nationals-to-protect-the-security-of-the-united-states/
12. https://www.presidency.ucsb.edu/documents/proclamation-10998-restricting-and-limiting-the-entry-foreign-nationals-protect-the
13. https://ng.usembassy.gov/mission-nigeria-update-on-visa-issuance/
14. https://ng.usembassy.gov/visas/
15. https://ng.usembassy.gov/revised-visa-reciprocity-policy-for-nigeria/
16. https://www.nafsa.org/regulatory-information/proclamation-december-16-2025-travel-ban-effective-january-1-2026
17. https://www.aila.org/library/dos-91-fr-6283-2-11-26 (seen in search; delegation of national interest authority)
18. https://www.icirnigeria.org/us-signals-visa-restrictions-review-for-nigeria/
19. https://www.visaverge.com/visa/us-mission-visa-rules-presidential-proclamations-10998-visa-suspensions-are-temporary/
20. https://jqklaw.com/nigerian-immigrants-2026-travel-ban-uscis-pause/
21. https://www.mytravelready.ai/blog/nigeria-usa-visa-guide-2026
22. https://americanbazaaronline.com/2026/10/04/us-visa-bond-program-20000-b1-b2-489343/
23. https://www.hio.harvard.edu/news/2025/09/us-government-instructs-visa-applicants-apply-their-country-residence (seen in search)
24. https://techcrunch.com/2023/09/19/yc-says-visa-challenges-hampering-participation-of-international-founders
25. https://startup.pk/can-a-pakistani-founder-actually-go-to-yc-the-visa-question-answered-honestly/
26. https://www.passright.com/the-ultimate-guide-for-startup-founders-best-visa-green-card-options-for-y-combinator-techstars-and-other-accelerator-founders-to-stay-in-the-u-s/
27. https://ardinalaw.com/u-s-visa-options-for-y-combinator-techstars-berkeley-skydeck-and-other-accelerator-founders/
28. https://www.beyondborderglobal.com/resources/o-1-visa-premium-processing
29. https://www.uatechjournal.com/y-combinator-opens-remote-access-to-ukrainian-defense-startups-for-winter-2026/ (body not returned; claim from search summary, unverified)
30. https://techcabal.com/2026/10/10/timon-founders-and-visa-hurdles/
31. https://visagrader.com/us-visa-appointment-wait-times/united-kingdom-of-great-britain-and-northern-ireland-gbr (seen in search; London figure unverified)

Entity, tax, Nigeria
32. https://hub.causo.ai/guides/non-us-founder-us-seed
33. https://turingventurecapital.com/manual/chapter/delaware-c-corp
34. https://www.zeccarosslaw.com/areas-served/best-us-incorporation-delaware-flip-international-founders
35. https://capbase.com/how-to-register-a-us-company-from-nigeria-in-10-minutes/
36. https://techcabal.com/2026/02/21/nigerias-new-capital-gains-tax-sparks-foreign-vc-anxiety/
37. https://www.legal500.com/intelligence/nigeria/tax/capital-gains-tax-under-the-nigeria-tax-act-2025-%E2%80%93-no-longer-business-as-usual
38. https://mondaq.com/nigeria/financial-services/1056846/doing-business-in-nigeria-the-relevance-of-the-certificate-of-capital-importation-to-foreign-investors-in-nigeria
39. https://thecable.ng/cbn-demands-transaction-evidence-for-repatriation-divestment-of-foreign-investments (seen in search)
40. https://nairametrics.com/wp-content/uploads/2013/02/GUIDELINES-FOR-DOING-BUSINESS-IN-NIGERIA.pdf (NIPC guidelines, seen in search)
41. https://cacregister.com.ng/blog/how-to-transfer-ownership-of-a-nigerian-company-to-a-foreign-investor-through-cac (seen in search)
42. https://techcabal.com/2022/01/27/what-african-founders-think-about-the-new-500000-y-combinator-deal/

African YC companies
43. https://yc-oss.github.io/api/companies/all.json
44. https://techcrunch.com/2022/03/29/yc-w22-batch-nets-24-african-startups-including-18-from-nigeria/
45. https://techcrunch.com/2024/12/07/as-yc-retreats-from-africa-alumni-launch-accelerators-to-fill-the-gap/
46. https://www.pulse.ng/story/a-look-at-nigerian-startups-that-got-into-the-famous-y-combinator-accelerator-2024072514053529106 (seen in search; count of 49)
47. https://techcabal.com/2023/08/02/chowcentral-ycombinator-summer-2023/

Sources marked "seen in search" were read through search summaries only, not opened in full; verify before
quoting them in any application.
