import sys
from io import StringIO
from unittest.mock import patch
from project import clean_month_input, get_veg, list_crops

def test_clean_month_input():
    assert clean_month_input("Jan") == "Jan"
    assert clean_month_input("jan") == "Jan"
    assert clean_month_input("January") == "Jan"
    assert clean_month_input("February") == "Feb"
    assert clean_month_input("Mar") == "Mar"
    assert clean_month_input("5") == "May"

    assert clean_month_input("Invalid") == "Invalid"


def test_get_veg():
    user_input = "Test Crop\nJan\nFeb\nMar\nTest Notes\n"
    input_values = user_input.split("\n")

    with patch("builtins.input", side_effect=input_values):
        vegetable = get_veg()

    assert vegetable.name == "Test crop"
    assert vegetable.sow == "Jan"
    assert vegetable.plantout == "Feb"
    assert vegetable.harvest == "Mar"
    assert vegetable.notes == "Test notes"

def test_list_crops():
    captured_output = StringIO()
    sys.stdout = captured_output

    try:
        list_crops() 
        printed_output = captured_output.getvalue()
    finally:
        sys.stdout = sys.__stdout__ 
    assert "Tomatoes" in printed_output