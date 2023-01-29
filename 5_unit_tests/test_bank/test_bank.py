from bank import value

def main():
	test_bank()

def test_bank():
	assert value("hello") == 0
	assert value("HelLo") == 0
	assert value("hell") == 20
	assert value("7") == 100
	
	

if __name__ == "__main__":
	main()