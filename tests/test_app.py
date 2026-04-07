"""Tests for the app entrypoint module."""
import os
import tempfile
from unittest.mock import patch

from shreddit.app import main


class TestImportSmoke:
    """Smoke tests to ensure the app module imports cleanly."""

    def test_import_main(self):
        """Test that the app module and main function can be imported.

        This catches issues like missing dependencies that only trigger
        when the module is loaded (e.g. pkg_resources on Python 3.14+).
        """
        assert callable(main)


class TestGenerateConfigs:
    """Tests for the -g/--generate-configs flag."""

    def test_generate_configs_creates_files(self):
        """Test that -g creates shreddit.yml and praw.ini in the current directory."""
        with tempfile.TemporaryDirectory() as tmpdir:
            original_dir = os.getcwd()
            os.chdir(tmpdir)
            try:
                with patch("sys.argv", ["shreddit", "-g"]):
                    main()
                assert os.path.isfile(os.path.join(tmpdir, "shreddit.yml"))
                assert os.path.isfile(os.path.join(tmpdir, "praw.ini"))
            finally:
                os.chdir(original_dir)
