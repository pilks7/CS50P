i = input("give me a filename\n").lower()
if i[-4:] == ".jpg":
	print("image/jpg")
elif i[-5:] == ".jpeg":
	print("image/jpeg")
elif i[-4:] == ".gif":
	print("image/gif")
elif i[-4:] == ".png":
	print("image/png")
elif i[-4:] == ".pdf":
	print("application/pdf")
elif i[-4:] == ".txt":
	print("application/txt")
elif i[-4:] == ".zip":
	print("application/zip")
else:
	print("application/octet-stream")