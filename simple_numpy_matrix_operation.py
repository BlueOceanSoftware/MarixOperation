# 2025-11-21
# simple matrix operations with numpy
import numpy as np
from numpy import array
# create a 2D array (matrix)
A = array([[1, 2], 
           [3, 4]])
print("Matrix A: \n", A)
print("Shape of A:", A.shape)
print(A[0, 1], A[0][1])  # Access element at first row, second column
B = array([[5, 6], 
           [7, 8],
           [9, 10]
           ])
print("shape of B:", B.shape)
print("A*B: \n" , np.dot(B, A))  # Matrix multiplication
print("A*B: \n" , B @ A)  # Matrix multiplication

# Transpose of A
print("Transpose of A: \n", A.T)

A[0,1] = 20  # Modify element at first row, second column
print("Modified Matrix A: \n", A)

C = array([[[1, 2, 3], 
           [7, 8, 9],
           [10, 11, 12]
           ],
           [[1, 2, 3], 
           [7, 8, 9],
           [10, 11, 12]
           ]])
print("3D Array C: \n", C)
print("Shape of C:", C.shape)