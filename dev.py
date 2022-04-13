# Method Overloading: How to use different number of arguments in the same function
class MethodOverloading: 

	def sum(self, x= None, y= None, z= None):
		if(x != None and y !=None and z!= None):

			s = x+y+z
			print(s)

		elif (x!=None and y!=None):
			s = x+y
			print(s)


m= MethodOverloading()

m.sum(30,50,70)