import sys
from working import convert
import pytest

def test_convert():
	assert convert("9 AM to 5 PM") == "09:00 to 17:00"
	assert convert("09:00 AM to 5:00 PM") == "09:00 to 17:00"
	with pytest.raises(ValueError):
		convert("12:60 PM to 5:00 AM")
	assert convert("12:00 AM to 9:00 PM") == "00:00 to 21:00"
	with pytest.raises(ValueError):
		convert("36 AM to 12 PM")
	with pytest.raises(ValueError):
		convert("9 AM 12 PM")	