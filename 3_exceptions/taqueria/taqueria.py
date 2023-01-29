menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

total = 0
for i, j in menu.items():
	print(f"{i}: $%.2f" %j)
print(f"Can I take your order please?\n(hold Ctrl+D to finish)")
menu = {k.lower(): v for k, v in menu.items()}
while True:
	try:
		user_input = input().lower()
		if user_input in menu:
			total += menu.get(user_input)
		else:
			print(f"Sorry, {user_input} is not on the menu today")
		print(f"Total so far = $%.2f" %total)	
	except EOFError:
		print(f"Total = $%.2f" %total)
		break