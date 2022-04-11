
def div (a,b):
	print (a/b)


def smart_div(func1):
	def innter(a,b):
		if a<b:
			a,b = b,a 
		return func1(a,b)

	return innter

div1 = smart_div(div)
div1(2,4)