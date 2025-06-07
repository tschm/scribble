import base64
import pytest
from app import create_download_link


class TestDownloadLink:
    """Tests for the create_download_link function in app.py."""

    def test_create_download_link_basic(self):
        """Test that the create_download_link function creates a valid HTML link."""
        # Test with basic parameters
        data = "Hello, world!"
        filename = "test.txt"
        result = create_download_link(data, filename)

        # Check that the result is a string
        assert isinstance(result, str)

        # Check that the result contains the expected elements
        assert 'download="test.txt"' in result
        assert 'href="data:text/plain;base64,' in result
        assert '>📥 Download test.txt</a>' in result

        # Check that the base64 encoding is correct
        b64_data = base64.b64encode(data.encode()).decode()
        assert b64_data in result

    def test_create_download_link_custom_mime(self):
        """Test that the create_download_link function works with custom MIME types."""
        # Test with a custom MIME type
        data = "<html><body>Hello</body></html>"
        filename = "test.html"
        mime = "text/html"
        result = create_download_link(data, filename, mime)

        # Check that the result contains the custom MIME type
        assert f'href="data:{mime};base64,' in result
