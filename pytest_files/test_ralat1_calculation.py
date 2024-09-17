import pytest
from ralat1_calculation import *
# import sys

# def test_myoutput(capsys):  # or use "capfd" for fd-level
#     print("hello")
#     sys.stderr.write("world\n")
#     captured = capsys.readouterr()
#     assert captured.out == "hello\n"
#     assert captured.err == "world\n"
#     print("next")
#     captured = capsys.readouterr()
#     assert captured.out == "next\n"

def test_calculation():
    result = calculation(10,2)
    assert result == 5

def test_get_input(monkeypatch):
    # Simulate user input for jejari and tinggi
    inputs = iter(["3", "7"])  # Mock input values
    
    # Mock the input() function
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    
    # Run the function and check the output
    result = get_input()
    assert result == (3, 7)

def test_main_calculation(monkeypatch, capsys):
    # Define a function to simulate multiple user inputs
    user_inputs = ["10","2"]

    def mock_input(_):
        return user_inputs.pop(0)

    # Use the function to simulate user input
    monkeypatch.setattr('builtins.input', mock_input)

    # Call the main function, which uses input() and prints the result
    main_calculation()

    # Capture the printed output
    captured = capsys.readouterr()
    assert captured.out.strip() == "Division = 5.0"

