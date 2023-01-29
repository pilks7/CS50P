import sys

def main():
	print(counter())

if len(sys.argv) < 2:
	sys.exit('Too few arguments')
elif len(sys.argv) > 2:
	sys.exit('Too many arguments')
elif sys.argv[1][-3:] != '.py':
	sys.exit('Not a python file')

try:
	with open(sys.argv[1], "r") as file:
		lines = file.readlines()
except FileNotFoundError:
	sys.exit('File does not exist')


def counter():
	linecount = 0
	for line in lines:
		# if '#' or '\n' not in line.lstrip().startswith():
		if line.lstrip().startswith('#') or not line.lstrip(): # second part returns False (-> else) if lstripped line contains any characters
			pass
		else:
			linecount += 1
	return linecount

if __name__ == '__main__':
	main()