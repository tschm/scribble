import pytest


@pytest.fixture()
def name():
    """
    This fixture provides the name input from the __input_name cell.
    """
    from app import __input_name

    _, definitions = __input_name.run()

    return definitions["name"]


@pytest.fixture()
def dropdown():
    """
    This fixture provides the dropdown input from the __input_function cell.
    """
    from app import __input_function

    _, definitions = __input_function.run()

    return definitions["dropdown"]


@pytest.fixture()
def event():
    """
    This fixture provides the event input from the __input_event cell.
    """
    from app import __input_event

    _, definitions = __input_event.run()

    return definitions["event"]


class TestInputs:
    """Tests for the input components in app.py."""

    def test_name_input(self, name):
        """Test that the name input is a text input."""
        # Check that the name input has the correct type
        assert str(type(name).__name__) == "text"

        # Print the type and dir of the name input for debugging
        print(f"Type of name: {type(name)}")
        print(f"Dir of name: {dir(name)}")

    def test_dropdown_input(self, dropdown):
        """Test that the dropdown input is a dropdown."""
        # Check that the dropdown input has the correct type
        assert str(type(dropdown).__name__) == "dropdown"

        # Print the type and dir of the dropdown input for debugging
        print(f"Type of dropdown: {type(dropdown)}")
        print(f"Dir of dropdown: {dir(dropdown)}")

    def test_event_input(self, event):
        """Test that the event input is a text input."""
        # Check that the event input has the correct type
        assert str(type(event).__name__) == "text"

        # Print the type and dir of the event input for debugging
        print(f"Type of event: {type(event)}")
        print(f"Dir of event: {dir(event)}")
