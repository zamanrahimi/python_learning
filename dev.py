

# How to read from file
f = open("file.py", "r")

print(f.readline())

#how to write into the file 

f1 = open("file1.txt", "w")
f1.write("Hello, this file should be written inside file1.txt. but first it should be created")

# how to append some data into the file 
f1 = open("file1.txt", "a")
f1.write("append ")

