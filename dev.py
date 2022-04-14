# Python - Binary search 

pos = -1
n = 10

# list
li = [10, 4, 5, 6]

# function 
def search(li, n):	
	i = 0
	while i< len(li):
		 
		if li[i] == n:
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