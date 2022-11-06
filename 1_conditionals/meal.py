def main():
	convert(input())

def convert(time):
	h, m = time.split(":")
	a = int(h) + int(m)/60
	if 7 <= a <= 8:
		print("breakfast time")
	elif 12 <= a <= 13:
		print("lunchtime")
	elif 18 <= a <= 19:
		print("dinnertime")

if __name__ == "__main__":
	main()