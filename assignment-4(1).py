#Construct a Python program using NumPy to generate a 4×4 identity matrix.
import numpy as np

x = np.eye(4)

print("Identity Matrix is:")
print(x)

#Develop a Python program to generate two 3×3 matrices filled with random integers (1 to 9), then perform matrix addition and matrix multiplication.
import numpy as np

x = np.random.randint(1,10,(3,3))
y = np.random.randint(1,10,(3,3))

print("Matrix X:")
print(x)

print("Matrix Y:")
print(y)

z = x + y
print("Addition:")
print(z)

m = x @ y
print("Multiplication:")
print(m)