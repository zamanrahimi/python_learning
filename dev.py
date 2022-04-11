def count(list): 

	even =0
	odd =0
	for i in list:
		if i%2==0:
			even +=1
		else:
			odd +=1
	return even, odd

list =[2,55,88,40,44]

even, odd = count(list)
print("The odd number is : {}".format(odd))
print ("The even number : {}".format(even))