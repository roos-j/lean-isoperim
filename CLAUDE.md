@AGENTS.md

For mathematical formalization, use `.claude/skills/autoformalize/SKILL.md`.

## Commits

Every commit: author = the user who is prompting (their name and email, e.g. from the session's
user identity or the repository history; set it with `git commit --author="Name <email>"`),
message exactly one line starting with `[claude]`, then a blank line and the single trailer
`Co-authored-by: Claude <noreply@anthropic.com>`. No session links or other trailers.
