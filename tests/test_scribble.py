import numpy as np

from pyscribble._scribble import __segment, series


def test_segment():
    """Test the __segment function."""
    # Create a simple array with two points
    points = np.array([0, 1+1j])

    # Get the segments
    segments = list(__segment(points, n=10))

    # Should be one segment (between the two points)
    assert len(segments) == 1

    # Each segment should have n points
    assert len(segments[0]) == 10

    # First point of the segment should be the first point of the input
    assert segments[0][0] == 0

    # Last point of the segment should be the second point of the input
    assert segments[0][-1] == 1+1j

    # Points should be evenly spaced
    # The spacing is 1/9 because we have 10 points from 0 to 1 (9 intervals)
    step = 1/9

    # Check a few intermediate points
    assert np.isclose(segments[0][1].real, step)
    assert np.isclose(segments[0][1].imag, step)
    assert np.isclose(segments[0][5].real, 5*step)
    assert np.isclose(segments[0][5].imag, 5*step)

def test_series_single_letter():
    """Test the series function with a single letter."""
    # Use a simple letter (A) and a simple function (identity)
    result = series("A", n=10, str="z")

    # The result should be a list
    assert isinstance(result, list)

    # The result should not be empty
    assert len(result) > 0

    # Each element in the result should be a numpy array
    for segment in result:
        assert isinstance(segment, np.ndarray)

def test_series_multiple_letters():
    """Test the series function with multiple letters."""
    # Use two simple letters (AB) and a simple function (identity)
    result = series("AB", n=10, str="z")

    # The result should be a list
    assert isinstance(result, list)

    # The result should not be empty
    assert len(result) > 0

    # Each element in the result should be a numpy array
    for segment in result:
        assert isinstance(segment, np.ndarray)

    # The result for multiple letters should be longer than for a single letter
    single_letter_result = series("A", n=10, str="z")
    assert len(result) > len(single_letter_result)

def test_series_with_function():
    """Test the series function with a non-trivial function."""
    # Use a simple letter (A) and a non-trivial function (z*z)
    result = series("A", n=10, str="z*z")

    # The result should be a list
    assert isinstance(result, list)

    # The result should not be empty
    assert len(result) > 0

    # Each element in the result should be a numpy array
    for segment in result:
        assert isinstance(segment, np.ndarray)

    # The function z*z should square each point
    # We can't easily test this directly, but we can check that the points are different
    # from the identity function
    identity_result = series("A", n=10, str="z")

    # The results should have the same length
    assert len(result) == len(identity_result)

    # But the points should be different
    # We'll check that at least one segment is different
    # We can't directly compare the segments because they are numpy arrays with complex values
    # So we'll convert them to strings and compare those
    assert any(str(result[i]) != str(identity_result[i]) for i in range(len(result)))
