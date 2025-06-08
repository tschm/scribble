"""Tests for the __input_event function in app.py."""
import marimo as mo

from app import __input_event, __input_function, __input_name


def test_input_event():
    """Test the functionality of processing an input event.

    Test its return format to
    ensure compliance with expectations.

    Ensures that the method processes a simulated input event (`__input_event.run`)
    and validates that the output is a tuple containing a dictionary with an `event`
    key.

    Raises
    ------
    AssertionError
        If the result is not a tuple or does not have a 'event' key in the second
        element of the tuple.

    """
    # Run the cell
    result = __input_event.run(mo=mo)

    # Check that the cell returns a tuple where the second element is a dictionary containing the event
    assert isinstance(result, tuple)
    assert len(result) == 2
    assert "event" in result[1]
    print(result[1]["event"])

def test_input_name():
    """Test the `run` method of the `__input_name` module.

    Ensure it returns a tuple
    with a length of 2, contains a key "name" in the second element, and prints its
    value.

    Raises
    ------
    AssertionError
        If the result is not a tuple, does not have a length of 2, or if the key
        "name" is not found in the second element.

    """
    result = __input_name.run(mo=mo)
    assert isinstance(result, tuple)
    assert len(result) == 2
    assert "name" in result[1]
    print(result[1]["name"])



def test_input_function():
    """Test the __input_function.run method's output and validates its structure.

    This function executes the __input_function.run method with the provided
    input parameters and verifies that the output meets the expected requirements.
    It checks if the output is a tuple, if the tuple length matches the expectation,
    and if a specific key ("dropdown") is present in the output dictionary.

    Raises:
        AssertionError: If the output of __input_function.run does not match
        the expected tuple structure or key requirements.

    """
    result = __input_function.run(mo=mo)
    assert isinstance(result, tuple)
    assert len(result) == 2
    assert "dropdown" in result[1]
    print(result[1]["dropdown"])
