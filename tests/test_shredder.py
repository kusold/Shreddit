"""Tests for the Shredder class."""
from unittest.mock import Mock, patch

from shreddit.shredder import Shredder


class TestShredderWhitelist:
    """Tests for whitelist checking functionality."""

    @patch('shreddit.shredder.praw.Reddit')
    def test_check_whitelist_by_subreddit(self, mock_reddit):
        """Test that items from whitelisted subreddits are identified correctly."""
        mock_reddit.return_value.user.me.return_value = Mock(name="testuser")

        config = {
            "hours": 24,
            "nuke_hours": 720,
            "item": "comments",
            "sort": "new",
            "verbose": False,
            "whitelist": ["test_subreddit"],
            "whitelist_ids": [],
            "whitelist_distinguished": False,
            "whitelist_gilded": False,
            "multi_whitelist": [],
            "blacklist": [],
            "multi_blacklist": [],
            "save_directory": None,
            "trial_run": True,
            "clear_vote": False,
            "replacement_format": "dot",
            "max_score": None,
            "keep_a_copy": False,
            "batch_cooldown": 10
        }

        shredder = Shredder(config, "default")

        # Create a mock item from the whitelisted subreddit
        item = Mock()
        item.subreddit = "test_subreddit"
        item.id = "abc123"
        item.distinguished = False
        item.gilded = False
        item.score = 1

        assert shredder._check_whitelist(item) is True

    @patch('shreddit.shredder.praw.Reddit')
    def test_check_whitelist_by_id(self, mock_reddit):
        """Test that items with whitelisted IDs are identified correctly."""
        mock_reddit.return_value.user.me.return_value = Mock(name="testuser")

        config = {
            "hours": 24,
            "nuke_hours": 720,
            "item": "comments",
            "sort": "new",
            "verbose": False,
            "whitelist": [],
            "whitelist_ids": ["abc123"],
            "whitelist_distinguished": False,
            "whitelist_gilded": False,
            "multi_whitelist": [],
            "blacklist": [],
            "multi_blacklist": [],
            "save_directory": None,
            "trial_run": True,
            "clear_vote": False,
            "replacement_format": "dot",
            "max_score": None,
            "keep_a_copy": False,
            "batch_cooldown": 10
        }

        shredder = Shredder(config, "default")

        # Create a mock item with the whitelisted ID
        item = Mock()
        item.subreddit = "random_subreddit"
        item.id = "abc123"
        item.distinguished = False
        item.gilded = False
        item.score = 1

        assert shredder._check_whitelist(item) is True

    @patch('shreddit.shredder.praw.Reddit')
    def test_check_whitelist_distinguished(self, mock_reddit):
        """Test that distinguished posts are whitelisted when enabled."""
        mock_reddit.return_value.user.me.return_value = Mock(name="testuser")

        config = {
            "hours": 24,
            "nuke_hours": 720,
            "item": "comments",
            "sort": "new",
            "verbose": False,
            "whitelist": [],
            "whitelist_ids": [],
            "whitelist_distinguished": True,
            "whitelist_gilded": False,
            "multi_whitelist": [],
            "blacklist": [],
            "multi_blacklist": [],
            "save_directory": None,
            "trial_run": True,
            "clear_vote": False,
            "replacement_format": "dot",
            "max_score": None,
            "keep_a_copy": False,
            "batch_cooldown": 10
        }

        shredder = Shredder(config, "default")

        # Create a mock distinguished item
        item = Mock()
        item.subreddit = "random_subreddit"
        item.id = "xyz789"
        item.distinguished = True
        item.gilded = False
        item.score = 1

        assert shredder._check_whitelist(item) is True

    @patch('shreddit.shredder.praw.Reddit')
    def test_check_whitelist_not_whitelisted(self, mock_reddit):
        """Test that non-whitelisted items return False."""
        mock_reddit.return_value.user.me.return_value = Mock(name="testuser")

        config = {
            "hours": 24,
            "nuke_hours": 720,
            "item": "comments",
            "sort": "new",
            "verbose": False,
            "whitelist": ["different_subreddit"],
            "whitelist_ids": ["different_id"],
            "whitelist_distinguished": False,
            "whitelist_gilded": False,
            "multi_whitelist": [],
            "blacklist": [],
            "multi_blacklist": [],
            "save_directory": None,
            "trial_run": True,
            "clear_vote": False,
            "replacement_format": "dot",
            "max_score": None,
            "keep_a_copy": False,
            "batch_cooldown": 10
        }

        shredder = Shredder(config, "default")

        # Create a mock item that doesn't match any whitelist criteria
        item = Mock()
        item.subreddit = "random_subreddit"
        item.id = "xyz789"
        item.distinguished = False
        item.gilded = False
        item.score = 1

        assert shredder._check_whitelist(item) is False


class TestShredderConnection:
    """Tests for connection and authentication."""

    @patch('shreddit.shredder.praw.Reddit')
    def test_connect_success(self, mock_reddit):
        """Test successful connection to Reddit."""
        mock_reddit.return_value.user.me.return_value = Mock(name="testuser")

        config = {
            "hours": 24,
            "nuke_hours": 720,
            "item": "comments",
            "sort": "new",
            "verbose": False,
            "whitelist": [],
            "whitelist_ids": [],
            "whitelist_distinguished": False,
            "whitelist_gilded": False,
            "multi_whitelist": [],
            "blacklist": [],
            "multi_blacklist": [],
            "save_directory": None,
            "trial_run": True,
            "clear_vote": False,
            "replacement_format": "dot",
            "max_score": None,
            "keep_a_copy": False,
            "batch_cooldown": 10
        }

        # Should not raise an exception
        shredder = Shredder(config, "default")
        assert shredder._username is not None
