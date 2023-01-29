import pytest
from numb3rs import validate
def test_validate():
	assert validate("255.1.1.1") == True
	assert validate("256.1.2.1") == False
	assert validate("0.0.0.0") == True
	assert validate("4.4") == False
	assert validate("one.two.three.four") == False
	assert validate("255.333.333.333") == False