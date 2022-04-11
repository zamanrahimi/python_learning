
def global_kw():
	global name
	name ="John, local"
	print(name)

global_kw()

print(name)