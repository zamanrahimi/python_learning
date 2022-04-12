class A: 

	def feature1(self):
		print("feature1")

class B: 

	def feature2(self):
		print("feature2")

class C(A,B): 

	def feature3(self):
		print("feature3")


c1 = C()
c1.feature1()
c1.feature2()
c1.feature3()
