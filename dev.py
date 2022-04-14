# Selection Sort: compare the first or min element with each element in the list
def sort(nums):
	for i in range (8):
		minpos = i
		for j in range(i,8):
			if nums[j] < nums[minpos]:
				minpos = j
				temp = nums[i]
				nums[i] = nums[minpos]
				nums[minpos] = temp

nums = [5,3,8,6,7,2,1,0]
sort(nums)

print(nums)