camel = input("camelCase:")
snake = "snake_case: "
for i in camel:
	if i.isupper():
		x += f"_{i}"
	else:
		x += i
print(snake.lower())