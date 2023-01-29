def main():
	i = input("greet me!").strip().lower()
	print(f"${value(i)}")

def value(i):
	if i.lower() == "hello":
		return (0)
	elif i[0].lower() == 'h':
		return (20)
	else:
		return (100)

if __name__ == "__main__":
	main()





