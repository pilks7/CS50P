from twttr import shorten

def main():
	test_shorten()

def test_shorten():
	assert shorten("TWitter") == "TWttr"
	assert shorten("Otter") == "ttr"
	

if __name__ == "__main__":
	main()