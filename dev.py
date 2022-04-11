def fact(n):
	if n ==0:
		return 1
		# fact called itself
	return n * fact(n-1)


print (fact(5) )