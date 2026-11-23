# Spec: docs/specs/spec-ir.md
from pathlib import Path
import unittest

from scripts.render_spec_ir import render


class SpecIrTest(unittest.TestCase):
    # Spec: docs/specs/spec-ir.md
    def test_checked_in_projections_match_their_graphs(self):
        for path in Path("docs/specs").glob("*.md"):
            with self.subTest(spec=path.name):
                source = path.read_text()
                self.assertIn("<!-- spec-ir:start -->", source)
                self.assertEqual(render(source), source)

    # Spec: docs/specs/spec-ir.md
    def test_unknown_endpoint_is_rejected(self):
        source = """```yaml spec-ir
id: sample
kind: flow
nodes:
  - {id: start, type: state, label: Start, meta: {}}
edges:
  - {from: start, to: missing, label: Continue, meta: {}}
```
"""
        with self.assertRaisesRegex(ValueError, "unknown endpoint"):
            render(source)
