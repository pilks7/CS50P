from tabulate import tabulate
import sys

try:
	table = []
	if len(sys.argv) < 2:
		sys.exit('Too few command-line arguments')
	elif len(sys.argv) > 2:
		sys.exit('Too many command-line arguments')
	with open(sys.argv[1], 'r') as file:
		if sys.argv[1][-4:] != '.csv':
			sys.exit('Not a valid csv file')
		for l in file:
			table.append(l.rstrip().split(","))
		print(tabulate(table, headers="firstrow", tablefmt="grid", showindex="true"))
except FileNotFoundError:
	sys.exit('File not found!')