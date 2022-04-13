class Salary: 

	def __init__(self, salary):
		self.salary = salary

	def __add__(self, other):

		return self.salary + other.salary


s1 = Salary(2000)
s2 = Salary(2000)
s3 = s1+s2

print(s3)