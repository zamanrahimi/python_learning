class Duck: 
	def sound(self):
		print("Quack Quack")

class Dog: 
	def sound(self):
		print("Woof Woof")

class Cat: 
	def sound(self):
		print("Mew Mew")


def all_ob(ojb):
	ojb.sound()

x1 = Duck()
x2 = Dog()
x = Cat()
all_ob(x)