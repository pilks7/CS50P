from fuel import gauge, convert
import pytest

def main():
	test_gauge()

def test_gauge():
	assert gauge(80) == "80%"
	assert gauge(89) == "89%"
	assert gauge(88) == "88%"
	assert gauge(100) == "F"
	assert gauge(1) == "E"
	assert gauge(99) == "F"

def test_convert():
	assert convert("4/5") == 4/5*100
	# assert convert("8/9") == 8/9*100
	# assert convert("7/8") == 7/8*100
	assert convert("1/1") == 1*100
	assert convert("0/5") == 0/5*100
	with pytest.raises(ValueError):
		convert("five/four")
	with pytest.raises(ZeroDivisionError):
		convert("4/0")


if __name__ == "__main__":
	main()