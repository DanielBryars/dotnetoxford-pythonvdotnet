"""One function. Five types. Zero changes."""
import numpy as np

def f(x):
    return x*x + 2*x

# Same function, every type
print("int:    ", f(3))                  # 15
print("float:  ", f(2.5))                # 11.25
print("complex:", f(1+2j))               # (-2+6j)
print("ndarray:", f(np.array([1,2,3])))  # [3 8 15]
print("matrix: ", f(np.eye(3) * 2))      # works on matrices too
