class A: 
	def __init__(self):
		print("init from A")

	def feature1(self):
		print("feature1")

class B (A): 

	def __init__(self):
		super().__init__()
		print("init from B")
		

	def feature2(self):
		print("feature2")


b = B()

# MRO = method resolution order: bottom to top, left to right