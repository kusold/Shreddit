"""Tests for utility functions."""
import pytest

from shreddit.util import ShredditError, get_sentence


class TestGetSentence:
    """Tests for the get_sentence function."""

    def test_get_sentence_returns_string(self):
        """Test that get_sentence returns a string."""
        result = get_sentence()
        assert isinstance(result, str)
        assert len(result) > 0

    def test_get_sentence_returns_different_values(self):
        """Test that get_sentence returns different values when called multiple times."""
        # Get 10 sentences and check that we get at least some variation
        sentences = [get_sentence() for _ in range(10)]
        unique_sentences = set(sentences)
        # Should have at least 2 different sentences (randomization should work)
        assert len(unique_sentences) >= 2


class TestShredditError:
    """Tests for the ShredditError exception."""

    def test_shreddit_error_with_message(self):
        """Test that ShredditError stores and displays the provided message."""
        error_msg = "Test error message"
        error = ShredditError(error_msg)
        assert error.value == error_msg
        assert str(error) == repr(error_msg)

    def test_shreddit_error_without_message(self):
        """Test that ShredditError has a default message when none is provided."""
        error = ShredditError()
        assert error.value == "No information provided"
        assert str(error) == repr("No information provided")

    def test_shreddit_error_is_exception(self):
        """Test that ShredditError is a subclass of Exception."""
        error = ShredditError("test")
        assert isinstance(error, Exception)

    def test_shreddit_error_can_be_raised(self):
        """Test that ShredditError can be raised and caught."""
        with pytest.raises(ShredditError) as exc_info:
            raise ShredditError("Custom error")
        assert exc_info.value.value == "Custom error"
