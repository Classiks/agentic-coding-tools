"""Check portable credential configuration without contacting Plane."""
import importlib.util
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

HELPER = Path(__file__).resolve().parents[2] / "skills/plane-records/scripts/plane_rest.py"
spec = importlib.util.spec_from_file_location("plane_rest", HELPER)
plane = importlib.util.module_from_spec(spec)
spec.loader.exec_module(plane)


class PlaneEnvironmentTests(unittest.TestCase):
    def test_complete_environment_needs_no_secrets_file(self):
        values = dict.fromkeys(plane.REQUIRED_ENVIRONMENT, "fixture")
        values["PLANE_SECRETS_FILE"] = "/nonexistent/secrets"
        with patch.dict(os.environ, values, clear=True):
            plane.load_environment()
            self.assertEqual(os.environ["PLANE_SERVICE_PASSWORD"], "fixture")

    def test_explicit_file_preserves_environment_and_literal_values(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "private.env"
            path.write_text("\n".join(f"{key}=from-file" for key in plane.REQUIRED_ENVIRONMENT if key != "PLANE_SERVICE_PASSWORD")
                            + "\nPLANE_SERVICE_PASSWORD=$(not-executed)=literal\n")
            with patch.dict(os.environ, {"PLANE_SECRETS_FILE": str(path),
                                         "PLANE_SERVICE_EMAIL": "override"}, clear=True):
                plane.load_environment()
                self.assertEqual(os.environ["PLANE_SERVICE_EMAIL"], "override")
                self.assertEqual(os.environ["PLANE_WORKSPACE_SLUG"], "from-file")
                self.assertEqual(os.environ["PLANE_SERVICE_PASSWORD"], "$(not-executed)=literal")

    def test_incomplete_environment_reports_names_without_values(self):
        with patch.dict(os.environ, {"PLANE_SERVICE_PASSWORD": "private-value"}, clear=True):
            with self.assertRaises(plane.PlaneRestError) as raised:
                plane.load_environment()
            self.assertIn("PLANE_BASE_URL", str(raised.exception))
            self.assertNotIn("private-value", str(raised.exception))

    def test_unreadable_configured_file_has_controlled_error(self):
        with patch.dict(os.environ, {"PLANE_SECRETS_FILE": "/nonexistent/secrets"}, clear=True):
            with self.assertRaisesRegex(plane.PlaneRestError, "Cannot read"):
                plane.load_environment()
