# Python - Linear search 

pos = -1
n = 6

# list
li = [10, 4, 5, 6]

# function 
def search(li, n):	
	i = 0
	for l in li:	 
		if l == n:
			global pos
			pos = i 
			return True
		i +=1 

	
	return False

# calling the function 
if search(li,n):
	print("found", n , "at position of ", pos)

else: 
	print("Not found")