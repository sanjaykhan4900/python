import numpy as np
arr= np.array([1,25,45,85,245,10,2,20,21,43])
#slicing
print(arr[1:6])

#negative slicing
print(arr[-5:-2])

#multi-dimensional array
arr2= np.array([[2,4,5,6,8],[9,45,23,8,6],[45,12,32,45,74]])

#dimension 
print(arr2.shape)

#iteration
for i in range(0,3):
    for j in range(0,5):
        print(arr2[i][j], end ="  ")
    print( )    

#split the array 
print(np.array_split(arr, 4))
