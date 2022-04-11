def list(**name):
	
	for k, v in name.items():
		print(k + " - ", v)


list(name='Ali', age=20, phone='4566')