camel = input("camelCase:")
snake = "snake_case: "

for i in camel:
	if i.isupper():
		snake += f"_{i}"
	else:
		snake += i
print(snake.lower())