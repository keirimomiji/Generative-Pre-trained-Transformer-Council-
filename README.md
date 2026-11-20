# Generative-Pre-trained-Transformer-Council-
A /council skill for ChatGPT, Claude, and Codex. Pick five advisors to debate your dilemma, weigh the trade-offs, and suggest a next step.

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

## Use the council

Send `/council` by itself to get started or include your dilemma and five advisors in one message.

> /council My Roblox game could launch next week with a small map, or I could delay a month to add more features. My advisors are Jane Jacobs, Grace Hopper, Hayao Miyazaki, Leslie Knope, and an indie game producer.

Start follow-ups with `/council` as well. The same panel can weigh in again.

## Standalone skill for ChatGPT

Where ChatGPT offers skill uploads, zip the [council skill folder](plugins/five-member-council/skills/council/) with `council/` at the top level of the archive. Open **Plugins → Skills → Create → Upload from your computer**. Select the skill with `@` in a chat and start your message with `/council`.

[ChatGPT skills setup](https://help.openai.com/en/articles/20001066-skills-in-chatgpt/)
