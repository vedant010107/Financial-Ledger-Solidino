import tempfile
import unittest
from pathlib import Path
from tools.brain import ingest, validate


class IngestionTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name) / "brain"
        (self.root / "inbox").mkdir(parents=True)
        (self.root / "index.md").write_text("# Index\n")
        (self.root / "log.md").write_text("# Log\n")
        self.note = dict(id="sqlite-locks", title="SQLite locks", author="fixture", owner="owner",
                         verification_assigned_to="checker", verified_by=None,
                         summary="A writer needs exclusive write access.",
                         sources=["SQLite transaction documentation"],
                         requirements=["FR-3"], links=["index"])

    def test_ingest_and_duplicate(self):
        ingest(self.root, self.note)
        validate(self.root)
        self.assertIn("[[sqlite-locks]]", (self.root / "log.md").read_text())
        with self.assertRaises(ValueError):
            ingest(self.root, self.note)
        self.assertEqual((self.root / "log.md").read_text().count("[[sqlite-locks]]"), 1)

    def test_unsafe_id(self):
        with self.assertRaises(ValueError):
            ingest(self.root, dict(self.note, id="../../outside"))
        self.assertFalse((self.root.parent / "outside.md").exists())

    def test_central_authorship(self):
        del self.note["author"]
        record = self.root.parent / "ai_author.txt"
        record.write_text("note | sqlite-locks | Codex\n")
        ingest(self.root, self.note)
        self.assertEqual(validate(self.root), 1)
        record.write_text("note | sqlite-locks-extra | Codex\n")
        with self.assertRaisesRegex(ValueError, "authorship"):
            validate(self.root)

    def test_verification_needs_evidence(self):
        self.note["verified_by"] = "checker"
        with self.assertRaisesRegex(ValueError, "verification"):
            ingest(self.root, self.note)
        (self.root.parent / "ai_author.txt").write_text(
            "verified | sqlite-locks | checker | Checked the writer limit.\n"
        )
        ingest(self.root, self.note)
        self.assertEqual(validate(self.root), 1)

    def test_broken_link(self):
        with self.assertRaises(ValueError):
            ingest(self.root, dict(self.note, links=["missing"]))
        self.assertFalse((self.root / "inbox/sqlite-locks.md").exists())
