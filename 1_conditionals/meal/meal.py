def main():
	convert(input("What time is it? "))
	if 7 <= a <= 8:
		print("breakfast time")
	elif 12 <= a <= 13:
		print("lunchtime")
	elif 18 <= a <= 19:
		print("dinnertime")


def convert(time):
	h, m = time.split(":")
	global a
	a = int(h) + int(m)/60
	return a
	


if __name__ == "__main__":
	main()