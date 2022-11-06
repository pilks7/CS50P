i = input()
x = int(i[0])
y = i[2]
z = int(i[4])

if y == '/':
	print(f"{x/z:.1f}")
elif y == '*':
	print(f"{x*z:.1f}")
elif y == '+':
	print(f"{x+z:.1f}")
elif y == '-':
	print(f"{x-z:.1f}")
else:
	print("hmm, something went wrong....")

