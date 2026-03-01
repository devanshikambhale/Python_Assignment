#Develop a NumPy program to multiply a 5×3 matrix by a 3×2 matrix and create a product matrix.Take input data from the user.import numpy as np

print("Enter elements for 5x3 matrix")

a = []
for i in range(5):
    row = []
    for j in range(3):
        x = int(input())
        row.append(x)
    a.append(row)

print("Enter elements for 3x2 matrix")

b = []
for i in range(3):
    row = []
    for j in range(2):
        y = int(input())
        row.append(y)
    b.append(row)

a = np.array(a)
b = np.array(b)

c = a @ b

print("Result matrix:")
print(c)