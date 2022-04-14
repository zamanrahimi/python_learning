# Python - Binary search 

# list
li = [10, 4, 5, 6]

# function 
def search(li, n):	
	i = 0
	while i< len(li):
		if li[i] == n:
			return True
		i +=1 

	
	return False

# calling the function 
if search(li, 6):
	print("found")

else: 
	print("Not found")