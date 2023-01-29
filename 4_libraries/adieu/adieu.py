import sys


names = []
adieu = 'Adieu, adieu, to '
try:
	while True:
		names.append(input("Name: "))
except EOFError:
	for name in names[:-1]:
		adieu += name + ', '
	adieu += f'and {names[-1]}'
	print(adieu)
	sys.exit
