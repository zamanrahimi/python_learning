#Method OverWriding: two method with the same name in two different classes 

class One: 

	def first(self):
		print("First method from class one")


		
class Two (One): 

	def first(self):
		print("First method from class Two")

t = Two()
t.first()


