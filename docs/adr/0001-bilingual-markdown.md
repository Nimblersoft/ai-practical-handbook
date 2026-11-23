---
title: "ADR-0001: Localized Markdown by concept"
type: adr
status: accepted
decided_by: Project requester
date: 2026-11-23
---

# Localized Markdown by concept

A reader who hears *deepfake* at work should be able to find it just as easily
as one looking for *ultrafalsificación*. Separate indexes make both terms
easy to find. An English landing page establishes the default and gives
Spanish readers an explicit way to switch.

Splitting a bilingual page into sibling language files lets readers share the
exact edition without a heading fragment and translate one language at a time.
Grouping by concept rather than under separate language trees keeps the
translations next to each other for review. The file naming follows
[AI Engineering From Scratch](https://github.com/rohitg00/ai-engineering-from-scratch).
See the [dictionary contract](../specs/dictionary.md) for navigation and layout.
