import os 
import sys
from PIL import Image, ImageOps


def main():
	if checking():
		lay_over()


def checking():
	accept_ext = [".jpg", ".jpeg", ".png"]
	if len(sys.argv) < 3:
		sys.exit('Too few arguments')
	elif len(sys.argv) > 3:
		sys.exit('Too many arguments')
	elif os.path.splitext(sys.argv[1])[1].lower() not in accept_ext or os.path.splitext(sys.argv[2])[1].lower() not in accept_ext:
		sys.exit(f"Accepted filetypes are: {accept_ext}")
	elif os.path.splitext(sys.argv[1])[1].lower() != os.path.splitext(sys.argv[2])[1].lower():
		sys.exit("Both files must be of same filetype")
	elif sys.argv[1] == sys.argv[2]:
		sys.exit("Files cannot be of same name")
	else:
		return True

def lay_over():
	try:
		with Image.open(sys.argv[1]) as picin:
			with Image.open("shirt.png") as overlay:
				picin = ImageOps.fit(picin, overlay.size)
				picin.paste(overlay, overlay)
				return picin.save(sys.argv[2])
	except FileNotFoundError:
		print("One or more files not found")

if __name__ == '__main__':
	main()