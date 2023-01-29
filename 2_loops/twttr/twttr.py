vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
x = input("Input: ")
for vowel in vowels:
	if vowel in x:
		x = x.replace(vowel, '')
print("Output:" + x)

# print(f"Output: {x.replace('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U', '')}")