import numpy as np
arr = np.array( [[ 1, 2, 3], [ 4, 2, 5]] )
print("Array is of type: ", type(arr))
print("No. of dimensions: ", arr.ndim) #printing array dimensions
print("Shape of array: ", arr.shape)
print("Size of array: ", arr.size)
print("Array stores elements of type: ", arr.dtype)
c=np.zeros((2,4))
b = np.full((3, 3), 6, dtype = 'complex')
print(b)
print(c)
e = np.random.random((2, 2))
print ("\nA random array:\n", e)
f = np.arange(0, 30, 5)
print ("\nA sequential array with steps of 5:\n", f)
g = np.linspace(0, 5, 10)
print ("\nA sequential array with 10 values between"
                                        "0 and 5:\n", g)
arr = np.array([[1, 2, 3, 4],
                [5, 2, 4, 2],
                [1, 2, 0, 1]])

newarr = arr.reshape(2, 2, 3)

print ("\nOriginal array:\n", arr)
print ("Reshaped array:\n", newarr)
arr = np.array([[1, 2, 3], [4, 5, 6]])
flarr = arr.flatten()

print ("\nOriginal array:\n", arr)
print ("Fattened array:\n", flarr)

#UNIVERSAL FUNCTIONS
arr1 = np.arange(4)
arr2 = np.array([10,20,30,40])
print("Exponent: {0}".format(np.exp(arr1)))
print(f"square root: {np.sqrt(arr2)}")
print(f"addition: {np.add(arr1,arr2)}")
dim_arr1 = np.arange(4).reshape((2,2))
dim_arr2 = np.array([[10,10],[10,10]])
#​print('Transpose:\\n {0}\\n'.format(np.transpose(dim_arr1)))
print("Transpose:\\n {0}\\n".format(np.transpose(dim_arr1)))
print(f"Cross product:\\n {np.cross(dim_arr1,dim_arr2)}\\n")
print(f"dot product:\\n {np.dot(dim_arr1,dim_arr2)}\\n")

arr1 = np.array([1, 2, 3, 4])
arr2 = arr1.copy()

print(arr2 is arr1)

arr2[0] = 2
arr2[3] = 2
arr2.shape = 2, 2
print("arr1=",arr1)
print("arr2=",arr2)

