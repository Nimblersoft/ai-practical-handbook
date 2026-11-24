# Connect a documentation tool with MCP

[Workflow index](../en.md) · [Español](es.md)

**Goal:** Have your assistant find an answer in Microsoft Learn and show you the page it used. Model Context Protocol (MCP) is a shared way for an AI app to talk to an outside tool. Here, Claude is the app; Microsoft Learn runs the service that searches the documentation.

**Before you start:** You need a Claude account or workspace that allows custom remote connectors. This example searches public documentation. You don't need a Microsoft login, an API key, or anything installed on your computer.

1. Open Claude's **Settings → Connectors**. Choose **Add custom connector** (it may be under **Add**). Name it `Microsoft Learn`.
2. Copy the server address from [Microsoft’s setup page](https://learn.microsoft.com/en-us/training/support/mcp): `https://learn.microsoft.com/api/mcp`. Put it in the connector’s URL field and add it. This is a service address, not a page to open in your browser.
3. Start a new chat. Open the tools or connectors menu and enable **Microsoft Learn** for the conversation. If asked to approve a tool call, check that it is searching or reading documentation.
4. Try: **“Use the Microsoft Learn connector to find a beginner’s explanation of multifactor authentication. Give me one sentence and the title and link of the page you used.”**

**Check the result:** Look for a Microsoft Learn tool call in the conversation, then open the returned page and compare it with the sentence. A plausible link alone does not show that the connector ran.

**If it doesn't work:** If **Add custom connector** is missing, check workspace permissions with the owner. If the answer came from ordinary web search, check that the connector is enabled in this chat and explicitly request it again. The connector can be disconnected from Settings when you're done.

[Claude’s connector guide](https://support.anthropic.com/en/articles/11175166-getting-started-with-custom-connectors-using-remote-mcp) · [What is grounding?](../../dictionary/entries/grounding/en.md)
