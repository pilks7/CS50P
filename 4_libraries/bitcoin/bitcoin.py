import requests
import sys
import json

try:
	if len(sys.argv) != 2 or not isinstance(float(sys.argv[1]), float):
		sys.exit("program requires exactly 1 argument of numerical format")

except ValueError:
	sys.exit("program requires exactly 1 argument of numerical format")

# try:
response = (requests.get("https://api.coindesk.com/v1/bpi/currentprice.json"))
rate = float(response.json()["bpi"]["USD"]["rate"].replace(",", ""))
rate = rate*float(sys.argv[1])
print(f"${rate:,.4f}")
# except:
# 	sys.exit("request issue")

