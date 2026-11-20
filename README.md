<p align="center">
  <img src="assets/readme-banner.gif" alt="Five-Member Council animated banner">
</p>

# Generative-Pre-trained-Transformer-Council
A /council skill for ChatGPT, Claude, and Codex. Five built-in advisor roles debate your dilemma, vote on the options, and suggest a next step.

## Install the plugin

### Claude app or Cowork

1. Open **Customize → Plugins → Add → Add marketplace**.
2. Choose **Add from a repository** and enter this URL.

   ```text
   https://github.com/keirimomiji/Generative-Pre-trained-Transformer-Council-
   ```

3. Add the **Five-Member Council** plugin from the new marketplace. Start a new chat and type `/council` or select the council skill from the slash menu.

[Claude plugin setup](https://support.claude.com/en/articles/13837440-use-plugins-in-claude)

### Claude Code

Run these commands **inside Claude Code**.

```text
/plugin marketplace add keirimomiji/Generative-Pre-trained-Transformer-Council-
/plugin install five-member-council@five-member-council
```

Start a new session and type `/council`. If another command already uses that name, use `/five-member-council:council`.

[Claude Code plugin setup](https://code.claude.com/docs/en/plugin-marketplaces)

### Codex CLI

Run these commands in your **terminal**.

```sh
codex plugin marketplace add keirimomiji/Generative-Pre-trained-Transformer-Council-
codex plugin add five-member-council@five-member-council
```

You can also open `/plugins` in Codex, select **Add Marketplace**, enter the same GitHub repository, and install **Five-Member Council**.

Start a new Codex session. Type `$` and select `five-member-council:council`, then begin your message with `/council`. For example, enter `$five-member-council:council /council` to start.

[Codex plugin commands](https://learn.chatgpt.com/docs/developer-commands)

## Update the plugin

Send `/council version` to see the version loaded in your session. On a local Claude Code or Codex installation, `/council update` refreshes the marketplace and updates Five-Member Council. In Codex, select the council skill first as shown above.

### Upgrade from v1.1.0 or earlier

The new chat command is available from **v1.2.0**. If your installed version is older, use the native plugin manager once.

**Claude Code terminal**

```sh
claude plugin marketplace update five-member-council
claude plugin update five-member-council@five-member-council
```

Run `/reload-plugins` in Claude Code or start a new session.

**Codex terminal**

```sh
codex plugin marketplace upgrade five-member-council
codex plugin add five-member-council@five-member-council
```

Start a new Codex session. These terminal commands also work if Python 3 is unavailable for the bundled updater.

For Claude on the web or in Cowork, manage the marketplace under **Customize → Plugins**. For ChatGPT, download the latest skill folder and upload it again.

## Use the council

Start with `/council` and describe your dilemma. Send `/council` alone if you'd like the plugin to ask for it. Use the same prefix on follow-ups.

| Advisor | What they bring |
| --- | --- |
| The Philosopher | Ethics, fairness, and long-term consequences |
| The Strategist | Planning, incentives, and practical risks |
| The Scientist | Evidence, uncertainty, and ways to test assumptions |
| The Visionary | Unconventional options and new possibilities |
| The Devil's Advocate | The strongest objection and what could go wrong |

## Worked example

> /council A small town museum has a grant that would cover either twelve Thursday evening openings or six Saturday pop-up exhibits at three branch libraries. Staff can run only one option. The goal is to reach people who rarely visit the museum. Which should we choose, and how should we tell whether it worked?

### Opening Statements

The two options address different barriers. Evening openings help people who can get to the museum but cannot visit during the day. Library exhibits bring the collection closer to people who may rarely consider visiting at all.

**The Philosopher.** I'd take the exhibit to the libraries. You can speak to someone who already uses a branch without asking them to plan a separate trip. That case rests on whether visitors get enough space and time to engage at the branch.

**The Strategist.** I'd add Thursday evenings. The exhibit is already installed, and staff can reuse their opening routine twelve times. If there are enough people waiting for hours that fit their schedules, this is a direct way to reach them. I would check how late they can realistically get to and from the museum.

**The Scientist.** My vote depends on what the museum means by “reach.” A library visitor who stops at one display might have a worthwhile encounter, and someone who spends forty minutes at the museum might already be a regular. I'd track meaningful encounters with people who rarely visit and collect the same basic information at every event.

**The Visionary.** I'd use the libraries and build each pop-up around one object and a question locals can answer. For example, show an old photograph of a familiar street and ask what has changed. The idea works only if the branches can offer a place to stop and talk.

**The Devil's Advocate.** I'd favor evenings if local groups can bring people who have never been. Library branches may draw plenty of foot traffic, but a busy branch can still be a poor exhibit venue. I want to know how many hours staff will spend transporting, setting up, and supervising the display before calling the pop-ups efficient.

### Cross-Examination

#### Who would actually come on Thursdays?

**The Philosopher → The Strategist.** Opening the building later helps people who already want to go. What gets someone who rarely thinks about the museum through the door after work?

**The Strategist.** Start with neighborhood groups whose members say daytime hours are the barrier. Ask each group when its members could come and whether it would share the opening dates.

**The Scientist.** Group leaders saying “people would love this” is weak evidence. Ask people at the branches and in those groups what kept them away on their last realistic chance to visit. If distance, transport, or lack of interest comes up more often than hours, your outreach plan is solving a different problem.

#### Does a short encounter count?

**The Devil's Advocate → The Visionary.** A queue near a photograph can look like a successful exhibit from across the room. What would tell you anyone engaged with it?

**The Visionary.** Count people who stop to talk about the object or offer a response to the exhibit question. Ask those participants how often they visit the museum. Count total traffic separately so we can see whether a busy branch actually helped.

**The Philosopher.** Some people will read and look closely without wanting to talk. Give them a written way to respond and collect a small sample of feedback so the measure leaves room for quieter visitors.

#### What would six pop-ups cost in staff time?

**The Strategist → The Visionary.** Twelve evenings use one setup. Six branch events need transport and coordination each time. How much museum time will each encounter cost?

**The Visionary.** Use the same portable display at all three branches and change the question or photograph where it helps. I'd ask each branch to name a staff contact and confirm space before we commit.

**The Devil's Advocate.** The space commitment is only half the answer. Ask museum staff to time a practice pack, setup, and teardown. If every event consumes a full staff day, estimate how much engagement each branch would need to justify that time.

### Rebuttals

**The Strategist** withdraws the assumption that later hours will reach new people on their own. They still vote for evenings if neighborhood groups can point to people who want to visit and name work hours as the barrier. The shorter setup makes that option easier to sustain once there is evidence of demand.

**The Visionary** accepts the Devil's Advocate's staffing check and the Philosopher's case for written feedback. The pop-ups now depend on a timed trial setup and a branch layout where people can linger.

**The Scientist** backs the pop-ups if the branches confirm space and staffing. Regular library visitors can tell the museum something it cannot learn from its own visitor book. The sample still won't represent residents who use neither institution.

### Final Vote

| Advisor | Vote | Reason |
| --- | --- | --- |
| The Philosopher | Library pop-ups | People can encounter the collection without planning another trip. |
| The Strategist | Thursday evenings | A verified scheduling barrier would justify twelve openings with one setup. |
| The Scientist | Library pop-ups | Branches offer a way to hear from people the museum seldom sees. |
| The Visionary | Library pop-ups | A portable, locally relevant exhibit can give people a reason to stop. |
| The Devil's Advocate | Thursday evenings | Repeated use of the existing exhibit avoids transport and setup at each event. |

**Tally — 3 for library pop-ups, 2 for Thursday evenings.**

### Council Verdict

Choose the library pop-ups if the branches can provide room for visitors to pause and the practice setup fits the staffing budget. Ask a few people at each branch what has kept them from visiting the museum. If those conversations point mostly to hours and neighborhood groups can show concrete interest in coming after work, choose Thursday evenings.

Before the first event, agree on how much staff time the museum can afford per encounter with someone who rarely visits. Track conversations or written responses, ask those participants how often they visit the museum, and log staff hours including travel and setup. Review the first two events before repeating the same layout. The evening option remains attractive if the logistics of the pop-ups leave too little time to engage with visitors.

*Of travel, opening hours, and interest in the exhibits, which barrier does the grant most need to address?*

## Another prompt to try

> /council A small bakery gets a reliable offer to supply two cafés every morning. Filling it would mean dropping Saturday custom cake orders, which bring in more per order but take longer to plan. The owner wants steadier weeks and has room for only one line of work. Which should the bakery keep, and what should the owner measure before committing?

## Standalone skill for ChatGPT

Where ChatGPT offers skill uploads, zip the [council skill folder](plugins/five-member-council/skills/council/) with `council/` at the top level of the archive. Open **Plugins → Skills → Create → Upload from your computer**. Select the skill with `@` in a chat and start your message with `/council`.

[ChatGPT skills setup](https://help.openai.com/en/articles/20001066-skills-in-chatgpt/)
