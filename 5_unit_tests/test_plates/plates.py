import string
import re

def main():
	plate = input("plate: ")
	if is_valid(plate):
		print("Valid")
	else:
		print("Invalid")

def is_valid(s):
	x = []
	if 1 < len(s) < 7 and not s[0:1].isnumeric() and not s[0:] in string.punctuation:
		for i in s:
			if i.isdigit():
				if i == '0':
					return False
				x = [u for e in s.split(i, 1) for u in (e, i)] ## magic line of code: splits list without losing delimiter
				for l in x[1:]:
					if l.isalpha():
						return False
		return True
	else:
		return False

if __name__ == "__main__":
	main()





