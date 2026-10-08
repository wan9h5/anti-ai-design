"""Regression tests for meaningful package corruption and publication hazards."""
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

SPEC = importlib.util.spec_from_file_location(
    "validate", Path(__file__).resolve().parents[1] / "scripts" / "validate.py"
)
validate = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(validate)

class PackageIntegrityTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="anti-ai-design-test-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()
        for relative in validate.REQUIRED:
            self.write(relative, "# Document\n")
        self.write("SKILL.md", "---\nname: anti-ai-design\ndescription: Create and review product interfaces.\n---\n# Skill\n")
        self.write("agents/openai.yaml", 'interface:\n  default_prompt: "Use $anti-ai-design."\n')
        source = {
            "id": "S01", "publisher": "Synthetic publisher", "title": "Fixture",
            "url": "https://example.org/design", "type": "guidance",
            "verification": "verified", "checked_on": "2026-10-08",
            "supports": "Synthetic test basis", "limits": "Fixture, not external evidence",
        }
        self.write("references/sources.json", json.dumps({"schema_version": 1, "sources": [source]}))
        self.write("references/evidence.md", "# Sources\n\n## S01\n")
        for number, catalog in enumerate(validate.CATALOGS, start=1):
            self.write("references/" + catalog, self.pattern(number))
        scenarios = []
        for mode in ("create", "review", "refactor"):
            scenarios.append({"id": mode, "mode": mode, "prompt": "Do work.",
                              "context": "Synthetic context", "must": ["Act"],
                              "must_not": ["Invent evidence"]})
        self.write("tests/scenarios.json", json.dumps({"schema_version": 1, "scenarios": scenarios}))

    def write(self, relative, text):
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")

    def pattern(self, number):
        identifier = "AP" + str(number).zfill(3)
        fields = "\n".join("- **" + name + ":** Synthetic value." for name in validate.FIELDS[:-1])
        return "# Catalog\n\n## " + identifier + ": Fixture\n\n" + fields + "\n- **Basis:** Guidance; [S01](evidence.md#s01).\n"

    def result(self):
        return validate.inspect_package(self.root)

    def test_valid_package(self):
        self.write("tests/artifacts/demo.html", '<html lang="en"><p>Clearly labeled synthetic demo.</p></html>\n')
        self.assertTrue(self.result()["ok"], self.result()["errors"])

    def test_missing_required_workflow(self):
        (self.root / "workflows/create.md").unlink()
        self.assertFalse(self.result()["ok"])

    def test_broken_local_reference(self):
        self.write("README.md", "# Readme\n[workflow](missing.md)\n")
        self.assertTrue(any("Broken local link" in e for e in self.result()["errors"]))

    def test_broken_source_anchor(self):
        self.write("README.md", "# Readme\n[Source](references/evidence.md#absent)\n")
        self.assertTrue(any("Broken anchor" in e for e in self.result()["errors"]))

    def test_link_cannot_escape_package(self):
        self.write("README.md", "# Readme\n[outside](../private.md)\n")
        self.assertTrue(any("escapes package" in e for e in self.result()["errors"]))

    def test_unknown_source(self):
        content = self.pattern(1).replace("[S01]", "[S99]")
        self.write("references/product-ia.md", content)
        self.assertTrue(any("Unknown source" in e for e in self.result()["errors"]))

    def test_duplicate_pattern(self):
        self.write("references/layout-density.md", self.pattern(1))
        self.assertTrue(any("Duplicate pattern" in e for e in self.result()["errors"]))

    def test_incomplete_exception_is_detected(self):
        content = self.pattern(1).replace("- **Exception:** Synthetic value.\n", "")
        self.write("references/product-ia.md", content)
        self.assertTrue(any("Missing Exception" in e for e in self.result()["errors"]))

    def test_limited_source_cannot_be_direct_guidance(self):
        path = self.root / "references/sources.json"
        content = json.loads(path.read_text())
        content["sources"][0]["verification"] = "limited"
        self.write("references/sources.json", json.dumps(content))
        self.assertTrue(any("Unverified direct basis" in e for e in self.result()["errors"]))

    def test_limited_source_can_support_explicit_hypothesis(self):
        path = self.root / "references/sources.json"
        content = json.loads(path.read_text())
        content["sources"][0]["verification"] = "limited"
        self.write("references/sources.json", json.dumps(content))
        for number, catalog in enumerate(validate.CATALOGS, start=1):
            self.write("references/" + catalog, self.pattern(number).replace("Guidance;", "Hypothesis;"))
        self.assertTrue(self.result()["ok"], self.result()["errors"])

    def test_environment_file_is_not_exportable(self):
        self.write(".env", "MODE=synthetic\n")
        self.assertTrue(any("Environment file" in e for e in self.result()["errors"]))

    def test_token_is_detected_without_echoing_value(self):
        synthetic_token = "ghp_" + "A" * 36
        self.write("README.md", synthetic_token)
        result = self.result()
        self.assertFalse(result["ok"])
        self.assertNotIn(synthetic_token, json.dumps(result))
        self.assertTrue(any("value withheld" in e for e in result["errors"]))

    def test_absolute_user_path_is_detected(self):
        synthetic_path = "C:" + chr(92) + "Users" + chr(92) + "Synthetic" + chr(92) + "private.txt"
        self.write("README.md", synthetic_path)
        self.assertTrue(any("absolute user path" in e for e in self.result()["errors"]))

    def test_private_image_is_not_exportable(self):
        self.write("private-screen.png", "synthetic")
        self.assertTrue(any("Unapproved artifact" in e for e in self.result()["errors"]))

    def test_malformed_source_registry(self):
        self.write("references/sources.json", "{not-json")
        self.assertTrue(any("source registry" in e for e in self.result()["errors"]))

    def test_missing_mode_in_scenarios(self):
        path = self.root / "tests/scenarios.json"
        data = json.loads(path.read_text())
        data["scenarios"] = [s for s in data["scenarios"] if s["mode"] != "create"]
        self.write("tests/scenarios.json", json.dumps(data))
        self.assertTrue(any("behavioral scenarios" in e for e in self.result()["errors"]))

if __name__ == "__main__":
    unittest.main()
