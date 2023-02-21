##imports: date. calendar?
import sys
import os.path
from os import path
from notify_run import Notify



def rereg():
	if len(sys.argv) > 1:
		if sys.argv[1] == '-r' or '--reset':
			os.remove('reg.txt')
			sys.exit()


def main():
	...

rereg()

if not path.isfile('reg.txt'):
	notify = Notify()
	reg = notify.register()
	print(reg)
	with open("reg.txt", 'x') as file:
		file.write(f'{reg}')








class Month:
	...

class Plant:
	...

if __name__ == '__main__':
	main()