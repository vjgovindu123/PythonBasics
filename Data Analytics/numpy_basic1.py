import timeit
import numpy as np
a=[1,2,3,4]
b=np.array(a)
print(b,type(b),b.ndim)

arr=np.array([1,2,3,4])
print(arr,arr.ndim,arr.dtype,arr.shape)

mat1=np.array([[1,2,3],[4,5,6],[7,8,9]])
mat2=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(mat1+mat2)
print(mat1.shape,mat2.ndim,mat2.dtype)
