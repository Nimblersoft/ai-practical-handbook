# Delegate a review to subagents

[Workflow index](../en.md) · [Español](es.md)

**Goal:** Check an event invitation against a venue note before sending it. A *subagent* is a helper your main assistant can assign a task to. Give each helper a question it can answer independently; keep the final comparison in the main conversation.

**Before you start:** Use an assistant that can actually launch subagents. This example uses Claude Code's built-in **Explore** helper, which can read files without editing them. Open a practice folder in Claude Code with these two plain-text files:

| File | Contents |
|---|---|
| `venue.txt` | The hall opens at 9:30. It seats 30. Lunch is not included. |
| `invite.txt` | Join us at 9:00. We have 35 places. Bring your lunch. |

1. Give the main assistant this assignment: **“Use two separate Explore subagents. Ask one to read only `venue.txt` and list the venue's constraints. Ask the other to read only `invite.txt` and list what we promise guests. Each must quote the wording and name the file. Don't change either file.”**
2. Check that the assistant shows two delegated tasks. If it returns two paragraphs without launching helpers, you have a single-assistant review; don't count it as two independent readings.
3. When both reports are back, ask: **“Compare the two reports. List contradictions separately from details that agree. Show the supporting quotes and leave the decision to me.”**

**Check the result:** You should find **two conflicts**: 9:00 versus a 9:30 opening, and 35 places versus 30 seats. Bringing lunch is consistent with lunch not being included. Reopen the two files to confirm the claims before correcting the invitation.

**If something is missing:** A helper may not have the main chat's context. Give it the exact filename and the question again. If your app has no subagents, you can still compare the files in two chats and bring the notes together yourself.

[Claude Code: subagents](https://code.claude.com/docs/en/sub-agents) · [What is an AI agent?](../../dictionary/entries/ai-agent/en.md)
