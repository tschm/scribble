from unittest.mock import patch

import pytest


@pytest.fixture()
def create_download_link():
    """
    This fixture provides the create_download_link function from the _download cell.
    """
    from app import _download

    _, definitions = _download.run()

    return definitions["create_download_link"]


class TestDownload:
    """Tests for the create_download_link function in the _download cell."""

    def test_create_download_link_returns_md(self, create_download_link):
        """Test that the create_download_link function returns a mo.md object."""
        result = create_download_link("test data", "test.txt")
        # Check that the result has the _repr_markdown_ method, which is a characteristic of mo.md objects
        assert hasattr(result, '_repr_markdown_')

    def test_create_download_link_with_custom_mime(self, create_download_link):
        """Test that the create_download_link function works with a custom MIME type."""
        result = create_download_link("test data", "test.html", mime="text/html")
        # Check that the result has the _repr_markdown_ method, which is a characteristic of mo.md objects
        assert hasattr(result, '_repr_markdown_')

    def test_create_download_link_content(self, create_download_link):
        """Test that the create_download_link function creates the correct HTML content."""
        with patch('base64.b64encode') as mock_b64encode:
            mock_b64encode.return_value = b'dGVzdCBkYXRh'  # 'test data' encoded
            result = create_download_link("test data", "test.txt")

            # Check that the result contains the expected elements
            html_content = result._repr_markdown_()
            assert 'download="test.txt"' in html_content
            assert 'data:text/plain;base64,dGVzdCBkYXRh' in html_content
            assert 'Download test.txt' in html_content
