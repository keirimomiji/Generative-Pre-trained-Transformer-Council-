# Generative-Pre-trained-Transformer-Council-
A /council skill for ChatGPT, Claude, and Codex. Pick five advisors to debate your dilemma, weigh the trade-offs, and suggest a next step.

## Use it

Send `/council` on its own to get started, then prefix your reply with `/council`. You can also supply everything in one message.

> /council My Roblox game could launch next week with a small map, or I could delay a month to add more features. My advisors are Jane Jacobs, Grace Hopper, Hayao Miyazaki, Leslie Knope, and an indie game producer.

Start follow-ups with `/council` as well. For example, `/council Ask the same panel how a two-week delay would change their advice.`

## Install

The shared instructions live in [five-member-council/SKILL.md](five-member-council/SKILL.md). Run these commands from the repository root.

### Claude Code

Install a version named `council` that Claude Code can invoke only through the user's slash command.

```sh
mkdir -p ~/.claude/skills/council
awk '
  /^name: five-member-council$/ {
    print "name: council"
    print "disable-model-invocation: true"
    next
  }
  { print }
' five-member-council/SKILL.md > ~/.claude/skills/council/SKILL.md
```

Type `/council` in Claude Code. For a single project, use `.claude/skills/council/SKILL.md` as the destination. [Claude Code skill docs](https://code.claude.com/docs/en/skills)

### Codex

```sh
mkdir -p ~/.agents/skills
cp -R five-member-council ~/.agents/skills/
```

Send the `/council` prefix as message text. Codex's native skill selector uses `$` or `/skills`, so some clients may reserve the leading slash for their own command menu. If the interactive CLI won't submit it, pass the prompt directly.

```sh
codex exec '/council'
```

To continue the same CLI session, replace `SESSION_ID` with the session identifier.

```sh
codex exec resume SESSION_ID '/council My dilemma is ...'
```

For a single repository, put the skill folder under that repository's `.agents/skills/`. [OpenAI skill docs](https://learn.chatgpt.com/docs/build-skills)

### Claude on the web

Create an upload archive with the shared skill folder at its top level.

```sh
zip -r five-member-council.zip five-member-council/
```

In Claude, go to **Customize → Skills → + → Create skill → Upload a skill**. Upload the archive, enable the skill, and start your message with `/council`. [Claude custom skills guide](https://support.claude.com/en/articles/12512180-use-skills-in-claude)

### ChatGPT

If Skills is available in your workspace, go to **Plugins → Skills → Create → Upload from your computer** and follow the upload prompts. Start your message with `/council`. You can also attach the skill using `@` in the same message. [ChatGPT skills guide](https://help.openai.com/en/articles/20001066-skills-in-chatgpt/)
