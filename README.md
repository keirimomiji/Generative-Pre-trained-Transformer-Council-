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

> /council Should I release my Roblox ship-building game next week with one small map, or wait a month to build a bigger one? I have limited time and a small testing group.

### Opening Statements

You have one small map, a small test group, and limited time. The decision depends on what the current map can teach you about the building loop and what another month of development would buy.

**The Philosopher.** I'd invite players next week and hold off on a public release. If you promise a game about designing ships, the first route should let players see a consequence of their design. I'd accept a short first session if players knew what they were signing up for and had a fair shot at making that discovery.

**The Strategist.** I'd open a limited beta next week. A month spent adding routes is a bad bet if new players can't get their first ship out of the dock. My bet depends on attracting a few genuine newcomers and having time to watch them. Without that, the launch gives us feedback we could already get from friends.

**The Scientist.** I'd run an observed playtest before deciding. Finishing a voyage could mean the ship editor is easy, the route is forgiving, or a friend coached the player through it. I want to see where an uncoached player hesitates and whether they have a reason to change their ship after sailing.

**The Visionary.** I'd keep the map and make one voyage reward two credible builds. A large hull could carry more cargo on the longer route, while a nimble hull could take a narrow shortcut. This only earns its place if both approaches work and a new player can understand their trade-off.

**The Devil's Advocate.** I'd postpone the public release and build a second challenge. Even if the first route supports two builds, one route might teach players a single trick. The case for spending another month depends on whether you can add a genuinely different demand on the same building system.

### Cross-Examination

#### What would public access teach you?

**The Devil's Advocate → The Strategist.** You say public access buys learning. What can you learn that you couldn't get by inviting the same number of strangers and watching them? Closing a beta won't undo someone's first impression.

**The Strategist.** A public session includes players who pick the game themselves. An invitation gives people a reason to stick around when they get confused. That's worth testing once we know they can get out of the dock.

**The Scientist.** Then separate the two questions. Watch uncoached invitees to find where they get stuck. Use a public beta to learn whether people who arrived on their own keep playing. If you open access while the first question is unresolved, early departures won't tell you whether the premise or the controls lost them.

#### Would the map reward different ships?

**The Philosopher → The Visionary.** What if the shortcut turns out to be the obvious best choice? You'd be asking people to experiment with a decision the map already made for them.

**The Visionary.** Make both builds worth running. The cargo ship should deliver more per trip, and the nimble ship should take less time. Check that neither wins on both measures before bringing in testers.

**The Philosopher.** That's a balance check. I also want to know whether players can see why a design did better. If the shortcut looks like a gap anybody can fit through, a player who gets wedged may blame the steering. Ask what they'd change and why before explaining the intended trade-off.

#### What would another month buy?

**The Strategist → The Devil's Advocate.** What would you put on the second map that justifies a month of work? An extra harbor still leaves the same building decisions.

**The Devil's Advocate.** Give players a reason to retire a ship that already worked. If the first delivery rewards capacity, a second one could demand tight turns. I'd consider adding that to the existing map. My objection is that we're betting on repeat building before we've seen a player face a new problem.

**The Strategist.** That changes the scope. If one extra delivery can expose the gap, I'd spend an evening prototyping it before committing a month to a second map.

### Rebuttals

**The Strategist** drops the immediate public launch after the Scientist separates onboarding from public interest. Next week's test should show where an uncoached player gets stuck before the team tries to measure voluntary return.

**The Visionary** accepts the Philosopher's point that a balanced route can still be hard to read. Testers should explain what their hull did for them and show what they'd change before anyone explains the route.

**The Devil's Advocate** drops the demand for a bigger map but keeps a higher bar for public release. They want newcomers to carry something they learned on the first trip into a second problem. The Scientist would open a limited beta sooner if players already choose to rebuild on the current route.

### Final Vote

| Advisor | Vote | Reason |
| --- | --- | --- |
| The Philosopher | Playtest next week, then open a limited beta if it passes | Players should be able to explain a consequence of their design. |
| The Strategist | Playtest next week, then open a limited beta if it passes | A short test can show where development time would matter most. |
| The Scientist | Playtest next week, then open a limited beta if it passes | Observe first-time players before using public behavior to judge the game. |
| The Visionary | Playtest next week, then open a limited beta if it passes | The existing map can reveal a design trade-off if both builds work. |
| The Devil's Advocate | Delay public access until a second challenge is tested | A single route may reward one build and give players little reason to return. |

**Tally — 4 for a playtest with a conditional public beta, 1 for testing a second challenge before public access.**

### Council Verdict

Keep next week as the playtest date. Invite a few people who have never seen the build, ask them to complete one delivery, and watch without coaching. Record where they get stuck and whether they start modifying their ship on their own.

If several players hit the same blocker, fix it and repeat the test. If they finish but see no reason to rebuild, prototype a second delivery on the same map with a different ship requirement. If newcomers can complete the loop and make a deliberate redesign for another run, open a limited public beta to see whether people who discover the game on their own also stick with it. The playtest can expose design problems, while the Devil's Advocate's concern about return visits stays open.

*What would make a player change a ship that already got them safely back to port?*

## Another prompt to try

> /council Our volunteer repair café has enough money for either a second monthly event or one shared toolkit that would speed up repairs. We already turn people away, and only four volunteers can diagnose electronics. Which should we fund, and what would prove we made the right choice?

## Standalone skill for ChatGPT

Where ChatGPT offers skill uploads, zip the [council skill folder](plugins/five-member-council/skills/council/) with `council/` at the top level of the archive. Open **Plugins → Skills → Create → Upload from your computer**. Select the skill with `@` in a chat and start your message with `/council`.

[ChatGPT skills setup](https://help.openai.com/en/articles/20001066-skills-in-chatgpt/)
