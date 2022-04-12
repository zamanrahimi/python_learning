class Computer: 
	
	def __init__(self, ram, cpu):
		self.ram = ram
		self.cpu =cpu

	def show(self):
		print(self.ram, self.cpu)

	class HP: 
		def __init__(self, hpRam, hpCpu):
			self.hpRam=hpRam
			self.hpCpu=hpCpu
		def show(self):
			print(self.hpRam, self.hpCpu)

c = Computer('21GB', '21GH')
hpc = Computer.HP('20GB', '100GB')

c.show()
hpc.show()