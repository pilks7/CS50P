due = 50
allowed = [25, 10, 5]
while due > 0:
	print(f"Amount due: {due}")
	i = int(input("insert coin: "))
	if i in allowed:
		due -= i
else:
	print(f"Change due: {-due}")


