import sys
import pyfiglet
import random

fonts = [
"3-d", "3x5", "5lineoblique", "slant",
"5lineoblique","alphabet", "banner3-D",
"doh", "isometric1", "letters",
"alligator", "bubble"
]



def main():
	try:
		if len(sys.argv) == 3:
			if sys.argv[1] == "-f" or "--font":
				print(pyfiglet.figlet_format(input(), font = sys.argv[2]))
		elif len(sys.argv) == 1:
			print(pyfiglet.figlet_format(input(), font = random.choice(fonts)))
		else:
			print("Command takes zero arguments to output a random font, else type -f or --font [name_of_font]")
	except:
		sys.exit

if __name__ == "__main__":
	main()