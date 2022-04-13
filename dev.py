#Multithreading 

from threading import * 
from time import sleep

class A (Thread):
	def run(self):
		for i in range(5):
			print("Hello")
			sleep(1)



class B (Thread):
	def run(self):
		for i in range(5):
			print("hi")
			sleep(1)


a1 = A()
a2 = B()
a1.start()
sleep(0.001)
a2.start()
