"""Exercise the public preparation command against disposable repository copies."""
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest

REPO = Path(__file__).resolve().parents[2]
EXPECTED_SKILLS = {
    "align", "coding-principles", "diagnose-bug", "domain-modeling", "grill-with-docs",
    "grilling", "guided-review", "project-knowledge", "reconcile-knowledge", "unslop",
}


class PrepareSkillsTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="skill selection #")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.source = self.root / "source's copy"
        shutil.copytree(REPO / "skills", self.source / "skills")
        (self.source / "scripts").mkdir()
        self.script = self.source / "scripts/prepare-skills.sh"
        shutil.copy2(REPO / "scripts/prepare-skills.sh", self.script)
        self.output = self.root / "nested output" / "bundle"

    def run_script(self, *args, output=None):
        return subprocess.run(
            ["bash", str(self.script), "--output", str(output or self.output), *args],
            cwd=self.root, text=True, capture_output=True,
        )

    def test_multiple_includes_repeated_and_complete_folders(self):
        result = self.run_script("--include", "guided-review", "align",
                                 "--include", "guided-review")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual({p.name for p in self.output.iterdir()},
                         {"guided-review", "align"})
        for name in ("guided-review", "align"):
            for source in (self.source / "skills" / name).rglob("*"):
                if source.is_file():
                    # Compare by relative skill path, including references and licenses.
                    copied = self.output / name / source.relative_to(self.source / "skills" / name)
                    self.assertEqual(copied.read_bytes(), source.read_bytes())
        self.assertIn("Reference to omitted skill: project-knowledge", result.stdout)
        self.assertFalse((self.output / "project-knowledge").exists())

    def test_multiple_exclusions_and_repeated_flags(self):
        result = self.run_script("--all", "--exclude", "grill-with-docs", "unslop",
                                 "--exclude", "grilling")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual({p.name for p in self.output.iterdir()},
                         EXPECTED_SKILLS - {"grill-with-docs", "unslop", "grilling"})

    def test_exclusions_win_independent_of_order(self):
        result = self.run_script("--exclude", "grilling", "--include", "grilling", "align")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual([p.name for p in self.output.iterdir()], ["align"])

    def test_full_bundle_has_no_omitted_references(self):
        result = self.run_script("--all")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertNotIn("Reference to omitted skill:", result.stdout)
        self.assertEqual({p.name for p in self.output.iterdir()}, EXPECTED_SKILLS)

    def test_invalid_selections_do_not_create_output(self):
        for args in [[], ["--all", "--include", "grilling"], ["--include"],
                     ["--all", "--exclude"], ["--include", "unknown"],
                     ["--all", "--exclude", "unknown"], ["--include", "../grilling"],
                     ["--include", "grilling", "--exclude", "grilling"], ["--bogus"]]:
            with self.subTest(args=args):
                result = self.run_script(*args)
                self.assertNotEqual(result.returncode, 0)
                self.assertFalse(self.output.parent.exists())

    def test_existing_output_and_symlink_are_preserved(self):
        self.output.mkdir(parents=True)
        marker = self.output / "keep.txt"
        marker.write_text("user content")
        result = self.run_script("--include", "grilling")
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(list(self.output.iterdir()), [marker])
        self.assertEqual(marker.read_text(), "user content")
        alias = self.root / "alias"
        alias.symlink_to(self.output, target_is_directory=True)
        self.assertNotEqual(self.run_script("--all", output=alias).returncode, 0)
        dangling = self.root / "dangling"
        dangling.symlink_to(self.root / "absent")
        self.assertNotEqual(self.run_script("--all", output=dangling).returncode, 0)
        self.assertTrue(dangling.is_symlink())

    def test_source_overlap_including_symlink_is_rejected(self):
        alias = self.root / "source-alias"
        alias.symlink_to(self.source / "skills", target_is_directory=True)
        for output in [self.source / "skills/new", alias / "new"]:
            result = self.run_script("--all", output=output)
            self.assertNotEqual(result.returncode, 0)
            self.assertFalse(output.exists())

    def test_missing_output_argument(self):
        result = subprocess.run(["bash", str(self.script), "--output"], capture_output=True)
        self.assertNotEqual(result.returncode, 0)


if __name__ == "__main__":
    unittest.main()
