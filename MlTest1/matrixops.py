# http://www.python-course.eu/numpy.php

import numpy as np
from timeit import Timer

cvalues = [25.3, 24.8, 26.9, 23.9]

C = np.array(cvalues)
print(C)

# print(C * 9 / 5 + 32)

# evenly spaced values
# arange([start,] stop[, step,], dtype=None)

a = np.arange(1, 10)
# print(a)

# print(np.arange(0.2, 10.4, 0.3))

# linspace(start, stop, num=50, endpoint=True, retstep=False)
# linspace returns an ndarray, consisting of 'num' equally spaced samples in the closed interval [start, stop] or the half-open interval [start, stop).
# print(np.linspace(1, 5))

"""
size_of_vec = 10000
def pure_python_version():
    X = range(size_of_vec)
    Y = range(size_of_vec)
    Z = []
    for i in range(len(X)):
        Z.append(X[i] + Y[i])

def numpy_version():
    X = np.arange(size_of_vec)
    Y = np.arange(size_of_vec)
    Z = X + Y
#timer_obj = Timer("x = x + 1", "x = 0")
timer_obj1 = Timer("pure_python_version()", "from __main__ import pure_python_version")
timer_obj2 = Timer("numpy_version()", "from __main__ import numpy_version")
print(timer_obj1.timeit(10))
print(timer_obj2.timeit(10))
"""

A = np.array([[3.4, 8.7, 9.9],
              [1.1, -7.8, -0.7],
              [4.1, 12.3, 4.8]])
print(A)
print(A.ndim)

x = np.array([[67, 63, 87],
              [77, 69, 59],
              [85, 87, 99],
              [79, 72, 71],
              [63, 89, 93],
              [68, 92, 78]])
print(np.shape(x))
print(x)

x.shape = (2, 9)
print(x)

F = np.array([1, 1, 2, 3, 5, 8, 13, 21])
# print the first element of F, i.e. the element with the index 0
print(F[0])
# print the last element of F
print(F[-1])
B = np.array([[[111, 112], [121, 122]],
              [[211, 212], [221, 222]],
              [[311, 312], [321, 322]]])
print(np.shape(B))
print(B)
print(B[0][1][0])
print(B[0, 1, 0])

x.shape = (3, 6)
print(x)
# slicing
print(x[:2, 3:])

print(np.eye(4))

A = np.array([[11, 12, 13], [21, 22, 23], [31, 32, 33]])
B = np.ones((3, 3))
print("Adding to arrays: ")
print(A + B)
print("\nMultiplying two arrays: ")
print(A * (B + 1))

print("\nDot product: ")
print(np.dot(A, B))

# use mat for matrices
MA = np.mat(A)
MB = np.mat(B)
R = MA * MB
print(R)

x = np.array([[0, 0, 1], [0, 1, 0], [1, 0, 0]])
y = ([3.65, 1.55, 3.42])
scalars = np.linalg.solve(x, y)
print(scalars)
