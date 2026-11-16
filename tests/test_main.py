import tempfile
import unittest
import zipfile
from pathlib import Path
from main import inspect_archive


class ZipSafetyTests(unittest.TestCase):
    def test_detects_traversal(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "sample.zip"
            with zipfile.ZipFile(path, "w") as archive:
                archive.writestr("../outside.txt", "bad")
            findings, _ = inspect_archive(path)
            self.assertTrue(any("traversal" in item[2] for item in findings))

    def test_safe_archive(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "safe.zip"
            with zipfile.ZipFile(path, "w") as archive:
                archive.writestr("docs/readme.txt", "hello")
            findings, _ = inspect_archive(path)
            self.assertEqual(findings, [])


if __name__ == "__main__":
    unittest.main()
