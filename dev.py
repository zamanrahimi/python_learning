# Python - Linear search 

pos = -1
n = 22

# list
li = [1, 4, 5, 6,7,10,22]

# function 
def search(li, n):	
	l=0
	u = len(li)-1

	while l<=u:
		mid = (l+u) //2
		if li[mid] ==n:
			global pos
			pos =mid
			return True
		else:
			if li[mid] < n:
				l = mid + 1
			else:
				u = mid - 1

# calling the function 
if search(li,n):
	print("found", n , "at position of ", pos)

else: 
	print("Not found")