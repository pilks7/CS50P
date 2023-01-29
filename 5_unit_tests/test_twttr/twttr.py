def main():
	i = input("Twwtrfy this: ")
	print("Output: ", shorten(i))


def shorten(word):
	vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
	for vowel in vowels:
		if vowel in word:
			word = word.replace(vowel, '')
	return (word)

if __name__ == "__main__":
	main()