from subprocess import Popen
p = Popen("m.bat", cwd=r"C:\Users\test\Desktop\python tutorial")
stdout, stderr = p.communicate()


def multiple_parameter(a, *b):
	c  = a 
	for i in b: 
		c = c + i

	print (c)


multiple_parameter(3,4,5,6,7,100)

