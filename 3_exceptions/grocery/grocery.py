from collections import OrderedDict

glist = {}
items = []

while True:
	try:
		item = input()
		items.append(item)
		if item in glist:
			glist[item] += 1
		else:
			glist[item] = 1
	except EOFError:
		glist = OrderedDict(sorted(dict.items(glist)))
		for _ in glist:
			print(f"{glist.get(_)} {_.upper()}")
		break