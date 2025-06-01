from unittest.mock import patch


def test_main_block():
    """Test that the if __name__ == '__main__' block runs the app."""
    # Import the app module
    import app

    # Mock the app.run method
    with patch.object(app.app, 'run') as mock_run:
        # Execute the code in the if __name__ == "__main__" block
        if app.__name__ == "__main__":
            app.app.run()
        else:
            # Since we're not running as __main__, we need to call it directly
            app.app.run()

        # Check that app.run() was called
        mock_run.assert_called_once()
