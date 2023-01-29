from validator_collection import validators, checkers, errors

def main():
	if checkers.is_email(input('Enter your email: ')):
		print('Valid')
	else:
		print('Invalid')


if __name__ == '__main__':
	main()