import sys



def main():
	
    while True:
        try:
            fraction = input("Give me a fraction (x/y): ")
            percentage = convert(fraction)
            print(gauge(percentage))
            break
        except ValueError as e:
            print(e)
            print("Please enter a valid fraction.")
        except ZeroDivisionError as e:
            print(e)
            print("Please enter a valid fraction.")

def convert(fraction):
	
	x, y = (fraction.split("/"))
	if not x.isnumeric() or not y.isnumeric():
		raise ValueError('Fraction must be in whole (positive) digits')
	elif int(y) == 0: 
		raise ZeroDivisionError("denominator cannot be zero")
	elif int(x) > int(y):
		raise ValueError("fraction must be less than/equal to one")

	else:
		return round(int(x)/int(y)*100)


def gauge(percentage):
	if 1 < percentage < 99:
		return f"{percentage}%"
	elif percentage <= 1:
		return "E"
	else:
		return "F"


if __name__ == "__main__":
	main()

