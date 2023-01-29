import sys
from pyfiglet import Figlet
import random


figlet = Figlet()

fonts = [
"3-d", "3x5", "5lineoblique", "slant",
"5lineoblique","alphabet", "banner3-D",
"doh", "isometric1", "letters",
"alligator", "bubble"
]

# fonts = [figlet.getFonts()]

def main():
	try:
		if len(sys.argv) == 1:
			figlet.setFont(font = random.choice(fonts))
			print(figlet.renderText(input("Type your message here: ")))
		elif len(sys.argv) == 3 and sys.argv[1] == "-f" or "--font":
			figlet.setFont(font = sys.argv[2])
			print(figlet.renderText(input("Type your message here: ")))
		else:
			sys.exit('first')
	except:
		sys.exit('except')

if __name__ == "__main__":
	main()

