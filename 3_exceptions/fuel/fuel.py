def main():
	percent("Give me a fraction (x/y): ")


def percent(prompt):
	while True:
		try:
			x, y = ''.join(input(prompt).split("/"))
			if int(x) > int(y) and int(y) != 0:
				continue
			z = int(x)/int(y)
		except ValueError:
			print("numerator and denominator must be integers")
		except ZeroDivisionError:
			print("denominator cannot be zero")
		else:
			pc = z*100
			if 1 < pc < 99:
				print(f"{int(round(pc, 0))}%")
				break
			elif pc <= 1:
				print("E")
				break
			else:
				print("F")
				break

if __name__ == "__main__":
	main()
