from numpy import * 


arr = array([3,5,7,7,3,2 ])

arr2 = arr.view() # copy and sync
arr2 = arr.copy() # copy and not sync
arr[0] = 10
print(arr)
print(arr2)