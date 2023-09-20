import random
from prettytable import from_csv
from prettytable import PrettyTable
import os
import sys
import csv

class Vegetable:
	
	def __init__(self, name, sow="", plantout="", harvest="", notes=""):
		self.name = name
		self.sow = sow
		self.plantout = plantout
		self.harvest = harvest
		self.notes = notes

	def __str__(self):
		return f"{self.name}"

	def __iter__(self):
		return iter([self.name, self.sow, self.plantout, self.harvest, self.notes])


def clean_month_input(input_month):
	month_mapping = {
		"january": "Jan",
		"february": "Feb",
		"march": "Mar",
		"april": "Apr",
		"may": "May",
		"june": "Jun",
		"july": "Jul",
		"august": "Aug",
		"september": "Sep",
		"october": "Oct",
		"november": "Nov",
		"december": "Dec"
	}
	
	cleaned_month = input_month.lower()
	
	# Check if input_month is already a valid abbreviation
	if cleaned_month in month_mapping.values():
		return cleaned_month  # Return it as is
	
	# Check if input_month is a numeric value
	if cleaned_month.isdigit():
		month_index = int(cleaned_month) - 1
		if 0 <= month_index < 12:
			return month_mapping[list(month_mapping.keys())[month_index]]  # Return it as is
	
	# Check if input_month is a full month name
	cleaned_month = month_mapping.get(cleaned_month)
	if cleaned_month:
		return cleaned_month  # Return it as is
	else:
		return input_month.capitalize()  # Capitalize the first letter and return it



def get_veg():
	print("Press enter to skip any fields.")
	crop = input("Crop Name: ").capitalize()
	sow = clean_month_input(input("Sow: "))
	plantout = clean_month_input(input("Plant out: "))
	harvests = clean_month_input(input("harvest: "))
	notes = input("Notes: ").capitalize()

	with open("veg.csv", "a") as my_veg:
		field_names = ["Crop", "Sow", "Plant out", "Harvest", "Notes"]
		writer = csv.writer(my_veg)
		# Write field names only if the file is empty
		if not os.path.isfile('veg.csv') or os.path.getsize("veg.csv") == 0:
			writer.writerow(field_names)
		writer.writerow([crop, sow, plantout, harvests, notes])
	return Vegetable(crop, sow, plantout, harvests, notes)

def list_crops(csvf):
	if not os.path.isfile(csvf) or os.path.getsize(csvf) == 0:
		print("You have no crops added, add crops at the main menu by pressing '1' ")
	else:
		with open(csvf, newline='') as csvfile:
			reader = csv.DictReader(csvfile)
			table = PrettyTable(reader.fieldnames)
			for row in reader:
				table.add_row([row[field] for field in reader.fieldnames])
		print(table)

def year_plan():
    with open("veg.csv", "r", newline='') as csvfile, open('veg3.csv', 'w', newline='') as out:
        reader = csv.reader(csvfile, delimiter=',')
        next(reader)
        month_dict = {}
        
        for row in reader:
            month = row[3]  # Assuming 'Harvest' is in the fourth column
            if month not in month_dict:
                month_dict[month] = [row]
            else:
                month_dict[month].append(row)
        
        field_names = ["Crop", "Sow", "Plant out", "Harvest", "Notes"]
        table = PrettyTable(field_names)
        
        for month in month_dict:
            rows = month_dict[month]
            if len(rows) > 1:
                random.shuffle(rows)
                month_dict[month] = [random.choice(rows)]
        
        for month in month_dict:
            row = month_dict[month][0]
            table.add_row([row[field_names.index(field)] for field in field_names])
        
        print(table)
			

def search():
	search = input("Type a crop to search: ").strip().capitalize()
	with open('veg.csv', 'r') as csvfile:
		reader = csv.reader(csvfile, delimiter=',')
		next(reader)
		for row in reader:
			if search == row[0]:
				table = PrettyTable()  # Create a new PrettyTable
				table.field_names = ['Crop', 'Sow', 'Plant out', 'Harvest', 'Notes']
				table.add_row(row)  # Add the matching row to the table
				print(table)
			else:
				if input('Not found. Would you like to add this crop now? Y/N').lower()[:1] in "y":
					get_veg()
				else:
					break

def delete():
	list_crops()
	choice = input('Please type which crop to delete. (To delete all, type "A")...').capitalize()

	if choice == 'A':
		if input('WARNING: This will delete all of your saved crops. Do you wish to continue? Y/N\n').lower()[:1] in "y":
			os.remove('veg.csv')
			print('All crops have been deleted')
	else:
		with open('veg.csv', 'r', newline='') as csvin, open('veg2.csv', 'w', newline='') as out:
			reader = csv.reader(csvin)
			writer = csv.writer(out)
			header = next(reader)
			writer.writerow(header)

			found = False
			for row in reader:
				if row[0].capitalize() != choice:
					writer.writerow(row)
				else:
					found = True

		os.remove('veg.csv')
		os.rename('veg2.csv', 'veg.csv')

		if found:
			print(f"{choice} has been deleted.")
		else:
			print(f"{choice} not found in the list.")




def main():
	while True:
		print(f"[1] Add a crop to your list")
		print(f"[2] List all crops currently in the program")
		print(f"[3] Create a yearly crop plan")
		print(f"[4] View a vegetable (or search for it)")
		print(f"[5] Delete crop(s)")
		print(f"[q] Enter q to quit.")
		choice = input("Please choose an option...").strip().lower()

		match choice:
			case '1':
				get_veg()
			case '2':
				list_crops('veg.csv')
			case '3':
				year_plan()
			case '4':
				search()
			case '5':
				delete()
			case 'q':
				sys.exit(0)
			case _:
				print('Invalid option. Please select an option')

if __name__ == '__main__':
	main()
