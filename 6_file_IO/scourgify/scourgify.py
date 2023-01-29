import sys
import csv

if len(sys.argv) < 3:
	sys.exit('Too few arguments')
if len(sys.argv) > 3:
	sys.exit('Too many arguments')
if sys.argv[1][-4:] != '.csv' or sys.argv[2][-4:] != '.csv':
	sys.exit('Files not in csv format')

with open(sys.argv[1]) as infile:
	students = []
	for l in infile:
		students.append(l.replace('"', '').strip().split(','))	#for each line in the csv strip newlines, replace double quotes with nothing, split into elements at commas and append to $students as a list ()
	for li in students[1:]:				#ignore index 0
		li[0], li[1] = li[1], li[0] 	# iterate through the lists in students  and swap index 0 and 1 (first and last name)
		li[0] = li[0].strip()
	students = students[1:]				#strip header


with open(sys.argv[2], 'w') as outfile:
	writer = csv.writer(outfile, delimiter=',')
	writer.writerow(['first', 'last', 'house'])
	writer.writerows(students)
	writer