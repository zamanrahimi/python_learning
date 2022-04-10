# How to have multiple argument in python function 
def multiple_parameter(a, *b):
	c  = a 
	for i in b: 
		c = c + i

	print (c)


multiple_parameter(3,4,5,6,7,100)

