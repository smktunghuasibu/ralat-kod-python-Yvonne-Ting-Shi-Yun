import pytest
from ralat2_cone import *
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

def test_kira_luas_permukaan_kon():
    result = kira_luas_permukaan_kon(2,3)
    assert result == 35.23

def test_dapat_jejari_tinggi(monkeypatch):
    # Simulate user input for jejari and tinggi
    inputs = iter(["3", "7"])  # Mock input values
    
    # Mock the input() function
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    
    # Run the function and check the output
    result = dapat_jejari_tinggi()
    assert result == (3, 7)

def test_main_cone(monkeypatch, capsys):
    # Define a function to simulate multiple user inputs
    user_inputs = ["2","3"]

    def mock_input(_):
        return user_inputs.pop(0)

    # Use the function to simulate user input
    monkeypatch.setattr('builtins.input', mock_input)

    # Call the main function, which uses input() and prints the result
    main_cone()

    # Capture the printed output
    captured = capsys.readouterr()
    assert captured.out.strip() == "luas permukaan kon = 35.23"

