from unittest.mock import MagicMock, patch

import pytest


@pytest.fixture()
def output_function():
    """
    This fixture provides the __output function from app.py.
    """
    from app import __output

    return __output


class MockValue:
    """A simple class to mock the value attribute of UI components."""
    def __init__(self, value):
        self.value = value


@pytest.fixture()
def mock_dependencies():
    """
    This fixture provides mock objects for the dependencies of the __output function.
    """
    # Create a mock Figure with a mock write_html method
    fig = MagicMock()
    fig.write_html = MagicMock()

    # Mock the create function
    create_mock = MagicMock(return_value=fig)

    # Mock the create_download_link function
    create_download_link_mock = MagicMock(return_value="<a>Download link</a>")

    # Mock the UI components
    dropdown_mock = MockValue("sinh(3*z)")
    event_mock = MockValue("wedding")
    name_mock = MockValue("Test")

    # Mock the mo module
    mo_mock = MagicMock()
    mo_mock.vstack = MagicMock(return_value="<div>Stacked content</div>")
    mo_mock.ui.plotly = MagicMock(return_value="<div>Plotly figure</div>")

    return {
        "create": create_mock,
        "create_download_link": create_download_link_mock,
        "dropdown": dropdown_mock,
        "event": event_mock,
        "mo": mo_mock,
        "name": name_mock,
        "fig": fig
    }


class TestOutput:
    """Tests for the __output cell in app.py."""

    def test_output_calls_create_with_correct_parameters(self, output_function, mock_dependencies):
        """Test that the __output function calls create with the correct parameters."""
        # Extract the dependencies
        create = mock_dependencies["create"]
        create_download_link = mock_dependencies["create_download_link"]
        dropdown = mock_dependencies["dropdown"]
        event = mock_dependencies["event"]
        mo = mock_dependencies["mo"]
        name = mock_dependencies["name"]

        # Call the output function
        output_function(create, create_download_link, dropdown=dropdown, event=event, mo=mo, name=name)


        # Check that create was called with the correct parameters
        create.assert_called_once_with(
            name=name.value,
            fct=dropdown.value,
            event=event.value,
            n=100
        )

    def test_output_calls_write_html(self, output_function, mock_dependencies):
        """Test that the __output function calls write_html on the figure."""
        # Extract the dependencies
        create = mock_dependencies["create"]
        create_download_link = mock_dependencies["create_download_link"]
        dropdown = mock_dependencies["dropdown"]
        event = mock_dependencies["event"]
        mo = mock_dependencies["mo"]
        name = mock_dependencies["name"]

        fig = mock_dependencies["fig"]

        # Patch the StringIO class
        with patch('io.StringIO') as mock_stringio:
            # Set up the mock StringIO instance
            mock_buf = MagicMock()
            mock_stringio.return_value = mock_buf

            # Call the output function
            output_function(create, create_download_link, dropdown=dropdown, event=event, mo=mo, name=name)

            # Check that write_html was called on the figure
            fig.write_html.assert_called_once_with(mock_buf, include_plotlyjs="cdn")

            # Check that seek(0) was called on the buffer
            mock_buf.seek.assert_called_once_with(0)

    def test_output_calls_create_download_link(self, output_function, mock_dependencies):
        """Test that the __output function calls create_download_link with the correct parameters."""
        # Extract the dependencies
        create = mock_dependencies["create"]
        create_download_link = mock_dependencies["create_download_link"]
        dropdown = mock_dependencies["dropdown"]
        event = mock_dependencies["event"]
        mo = mock_dependencies["mo"]
        name = mock_dependencies["name"]

        # Patch the StringIO class
        with patch('io.StringIO') as mock_stringio:
            # Set up the mock StringIO instance
            mock_buf = MagicMock()
            mock_buf.read.return_value = "HTML content"
            mock_stringio.return_value = mock_buf

            # Call the output function
            output_function(create, create_download_link, dropdown, event, mo=mo, name=name)

            # Check that create_download_link was called with the correct parameters
            create_download_link.assert_called_once_with(
                data="HTML content",
                filename=f"{name.value}_{event.value}_plot.html"
            )

    def test_output_calls_vstack(self, output_function, mock_dependencies):
        """Test that the __output function calls mo.vstack with the correct parameters."""
        # Extract the dependencies
        create = mock_dependencies["create"]
        create_download_link = mock_dependencies["create_download_link"]
        dropdown = mock_dependencies["dropdown"]
        event = mock_dependencies["event"]
        mo = mock_dependencies["mo"]
        name = mock_dependencies["name"]
        # Call the output function
        output_function(create, create_download_link, dropdown, event=event, mo=mo, name=name)


        # Check that mo.vstack was called with a list containing mo.ui.plotly and create_download_link
        mo.vstack.assert_called_once()
        args = mo.vstack.call_args[0][0]
        assert len(args) == 2
        assert args[0] == mo.ui.plotly.return_value
        assert args[1] == create_download_link.return_value

    def test_output_function_return(self, output_function, mock_dependencies):
        """Test that the __output function returns None."""
        # Extract the dependencies
        create = mock_dependencies["create"]
        create_download_link = mock_dependencies["create_download_link"]
        dropdown = mock_dependencies["dropdown"]
        event = mock_dependencies["event"]
        mo = mock_dependencies["mo"]
        name = mock_dependencies["name"]

        # Set the return value of mo.vstack to None
        mo.vstack.return_value = None

        # Call the output function and check the return value
        result = output_function(create, create_download_link, dropdown, event, mo=mo, name=name)
        assert result is None
