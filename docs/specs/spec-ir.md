---
title: "Spec: Spec-IR renderer"
type: spec
status: active
covers: scripts/render_spec_ir.py
last_checked: 2026-11-23
---

# Spec-IR renderer

[Authoring guide](../spec-ir.md)

```yaml spec-ir
id: spec-ir-render
kind: flow
nodes:
  - {id: input, type: input, label: Read Markdown, meta: {encoding: UTF-8}}
  - {id: validate, type: operation, label: Validate Spec-IR fences, meta: {graph_kinds: [flow, state, api, data], constraints: Reject duplicate IDs and keys, reference_rule: Edge endpoints must name nodes in their graph}}
  - {id: render, type: output, label: Replace marked Mermaid projections, meta: {preserve: Unmarked text and line endings, repeat_runs: Byte-identical result}}
  - {id: error, type: output, label: Report invalid input, meta: {result: Nonzero exit without writing the document}}
edges:
  - {from: input, to: validate, label: Find annotated fences, meta: {}}
  - {from: validate, to: render, label: All graphs and markers valid, meta: {}}
  - {from: validate, to: error, label: Invalid graph or generated marker, meta: {}}
```
<!-- spec-ir:start -->
```mermaid
flowchart TD
    N0["Read#32;Markdown"]
    N1["Validate#32;Spec#45;IR#32;fences"]
    N2["Replace#32;marked#32;Mermaid#32;projections"]
    N3["Report#32;invalid#32;input"]
    N0 -->|"Find#32;annotated#32;fences"| N1
    N1 -->|"All#32;graphs#32;and#32;markers#32;valid"| N2
    N1 -->|"Invalid#32;graph#32;or#32;generated#32;marker"| N3
```
<!-- spec-ir:end -->
