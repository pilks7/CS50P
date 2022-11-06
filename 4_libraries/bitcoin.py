import requests
import sys
import json

try:
	if len(sys.argv) != 2 or not isinstance(float(sys.argv[1]), float):
		print("program requires exactly 1 argument of numerical format")
		sys.exit()

except ValueError:
	print("program requires exactly 1 argument of numerical format")
	sys.exit()

try:
	response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
	rate = float(response.json()["bpi"]["USD"]["rate"].replace(",", ""))
	print(f"${rate:,}")
except:
	sys.exit("request issue")

