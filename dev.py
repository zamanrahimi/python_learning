class Computer:

	def __init__(self,ram, core):
		self.ram = core 
		self.core = ram 
		

	def config(self):
		print("Details", self.ram, self.core)


com1 = Computer('2GB RAM', 'CORI7')

com1.config()