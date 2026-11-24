# Spec: docs/specs/dictionary.md
from pathlib import Path
import re
import unicodedata
import unittest
from urllib.parse import unquote, urlsplit

from markdown_it import MarkdownIt


ROOT = Path(__file__).resolve().parents[1]
DICTIONARY = ROOT / "dictionary"
ENTRIES = set((DICTIONARY / "entries").iterdir())
LANGUAGES = {
    "en": ("es", "Example", "See also"),
    "es": ("en", "Ejemplo", "Véase también"),
}
MARKDOWN = MarkdownIt()


# Spec: docs/specs/dictionary.md
def links(text):
    for token in MARKDOWN.parse(text):
        for child in token.children or ():
            if child.type == "link_open":
                yield child.attrGet("href")


# Spec: docs/specs/dictionary.md
def alphabetical(text):
    decomposed = unicodedata.normalize("NFD", text.casefold())
    return "".join(char for char in decomposed if not unicodedata.combining(char))


class DictionaryTest(unittest.TestCase):
    # Spec: docs/specs/dictionary.md
    def test_home_defaults_to_english(self):
        reader_links = [href for href in links((ROOT / "README.md").read_text())
                        if href.startswith("dictionary/")]
        self.assertEqual(reader_links[:2], ["dictionary/en.md", "dictionary/es.md"])
        self.assertTrue(reader_links[2:])
        self.assertTrue(all(href.endswith("/en.md") for href in reader_links[2:]))

    # Spec: docs/specs/dictionary.md
    def test_both_indexes_list_each_entry_once_in_alphabetical_order(self):
        self.assertTrue(ENTRIES)
        for code, (other, _, _) in LANGUAGES.items():
            index = (DICTIONARY / f"{code}.md").read_text()
            rows = re.findall(r"^- \[([^\]]+)\]\(([^)]+)\)$", index, re.M)
            with self.subTest(language=code):
                labels = [label.split(" (", 1)[0] for label, _ in rows]
                self.assertEqual(labels, sorted(labels, key=alphabetical))
                self.assertCountEqual([url for _, url in rows],
                                      [f"entries/{entry.name}/{code}.md" for entry in ENTRIES])
                self.assertIn(f"{other}.md", links(index))
                self.assertIn(f"sources/{code}.md", links(index))

    # Spec: docs/specs/dictionary.md
    def test_entry_folders_have_complete_editions_and_stay_in_language(self):
        for entry in sorted(ENTRIES):
            with self.subTest(entry=entry.name):
                self.assertTrue(entry.is_dir())
                self.assertRegex(entry.name, r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
                self.assertEqual({page.name for page in entry.iterdir()}, {"en.md", "es.md"})
            for code, (other, example, related) in LANGUAGES.items():
                with self.subTest(entry=entry.name, language=code):
                    heading, nav, body = (entry / f"{code}.md").read_text().split("\n\n", 2)
                    self.assertRegex(heading, r"^# \S")
                    self.assertEqual(set(links(nav)), {f"../../{code}.md", f"{other}.md"})
                    self.assertRegex(body, r"^\*\*[^*\n]+\*\* \S")
                    self.assertRegex(body, rf"(?m)^\*\*{example}:\*\* \S")
                    related_line = re.search(rf"(?m)^\*\*{related}:\*\* .+$", body)
                    self.assertIsNotNone(related_line)
                    targets = list(links(related_line[0]))
                    self.assertTrue(targets)
                    allowed = {f"../{sibling.name}/{code}.md" for sibling in ENTRIES - {entry}}
                    self.assertTrue(set(targets) <= allowed, targets)

    # Spec: docs/specs/dictionary.md
    def test_reader_navigation_has_no_broken_local_links(self):
        pages = [ROOT / "README.md", *DICTIONARY.rglob("*.md"), *(ROOT / "workflows").rglob("*.md")]
        for page in pages:
            for href in links(page.read_text()):
                reference = urlsplit(href)
                if reference.scheme or reference.netloc:
                    continue
                target = page.parent / unquote(reference.path) if reference.path else page
                with self.subTest(page=page.relative_to(ROOT), href=href):
                    self.assertTrue(target.is_file())
                    self.assertFalse(reference.fragment, "Link directly to the language file")

    # Spec: docs/specs/workflows.md
    def test_workflows_are_reachable_in_both_languages(self):
        root = ROOT / "workflows"
        guides = {p.name for p in root.iterdir() if p.is_dir()}
        self.assertTrue({"connect-mcp", "delegate-to-subagents", "check-an-answer"} <= guides)
        home = list(links((ROOT / "README.md").read_text()))
        self.assertLess(home.index("workflows/en.md"), home.index("workflows/es.md"))
        for code, (other, _, _) in LANGUAGES.items():
            index = list(links((root / f"{code}.md").read_text()))
            self.assertCountEqual([href for href in index if href.split("/")[0] in guides],
                                  [f"{guide}/{code}.md" for guide in guides])
            self.assertIn(f"{other}.md", index)
            for guide in guides:
                with self.subTest(guide=guide, language=code):
                    page = (root / guide / f"{code}.md").read_text()
                    self.assertIn(f"{other}.md", links(page))
                    self.assertIn(f"../{code}.md", links(page))
                    concepts = [href for href in links(page) if "/dictionary/" in href]
                    self.assertTrue(concepts and all(href.endswith(f"/{code}.md") for href in concepts))
