#how to copy data from file.py into file1.txt

f1 = open("file.py", "r")
f2 = open("file1.txt", "w")


for data in f1:
	f2.write(data)