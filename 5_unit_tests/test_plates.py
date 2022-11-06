from plates import is_valid

def main():
	test_is_valid()

def test_is_valid():
	assert is_valid("AAA222") == True
	assert is_valid("AAA22A") == True
	assert is_valid("0aaa22") == False
	assert is_valid("A.B20") == False

if __name__ == "__main__":
	main()