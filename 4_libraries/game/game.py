import sys
import random
while True:
	try:
		n = int(input("Choose a level: "))
		break
	except ValueError:
		print("Level must be a number................")
correct = random.randint(1, n)

while True:
	guess = int(input("Guess the number: "))
	if guess > correct:
		print("Too Large!")
		continue
	elif guess < correct:
		print("Too Small!")
		continue
	else:
		print("Just right!")
		break
		sys.exit