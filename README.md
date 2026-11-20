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

## Example

> /council Should I release my Roblox ship-building game next week with one small map, or wait a month to build a bigger one? I have limited time and a small testing group.

### Opening Statements

- **The Philosopher** supports a beta if players know what they're signing up for. Their first session should deliver the ship-building experience the game promises.
- **The Strategist** favors releasing next week. A small trial gives you time to fix the problems you actually see.
- **The Scientist** wants to watch newcomers build and launch a ship without help before deciding how widely to release.
- **The Visionary** proposes one distinctive challenge on the small map so players have a reason to try different ship designs.
- **The Devil's Advocate** favors waiting. A good session with experienced testers could hide how confusing the game feels to a first-time player.

### Cross-Examination

**The Devil's Advocate to The Strategist.** If your usual testers already know how to build ships, what would their success tell you about a public launch?

**The Philosopher to The Visionary.** Can a player reach your signature challenge before they need someone to explain the controls?

### Rebuttals

**The Strategist** changes the proposal from a public beta to an invite-only test that includes players new to the genre.

**The Visionary** makes launching a starter ship the first step of the challenge. **The Devil's Advocate** keeps their objection. Finding a few new testers still leaves little margin to fix what they uncover before next week.

### Final Vote

| Advisor | Vote | Reason |
| --- | --- | --- |
| The Philosopher | Invite-only beta next week | Clear expectations make an early trial fair to players. |
| The Strategist | Invite-only beta next week | The limited rollout is easy to pause. |
| The Scientist | Invite-only beta next week | First-time players can show where onboarding breaks. |
| The Visionary | Invite-only beta next week | One challenge is enough to test whether ship design feels rewarding. |
| The Devil's Advocate | Wait a month | More time to fix onboarding lowers the risk of losing the first group of players. |

**Tally — 4 invite-only beta next week, 1 wait a month.**

### Council Verdict

Run an invite-only beta next week with one small map and recruit a few players who have never seen the game. Watch where they struggle to build and launch their first ship. If they repeatedly stall at the same step, fix it and test again before opening the beta. The dissent is that your group may be too small to spot every rough edge.

*What must a first-time player experience before their feedback tells you whether building ships is fun?*

## Standalone skill for ChatGPT

Where ChatGPT offers skill uploads, zip the [council skill folder](plugins/five-member-council/skills/council/) with `council/` at the top level of the archive. Open **Plugins → Skills → Create → Upload from your computer**. Select the skill with `@` in a chat and start your message with `/council`.

[ChatGPT skills setup](https://help.openai.com/en/articles/20001066-skills-in-chatgpt/)
