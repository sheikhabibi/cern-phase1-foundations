import numpy as np
import time

X = np.random.randn(1000,50)     # 1000 samples having 50 features each
W = np.random.randn(50,10)       # weights
b = np.random.randn(10)          # biases
print(np.shape(b))

def forwardPass(x,w,b):
    return(np.matmul(x,w)+b)

Z = forwardPass(X,W,b)
print(f"  Range before applying ReLU: {Z.min():.2f} to {Z.max():.2f}")
# apply activation function
A = np.maximum(Z,0)
print(f"  Range after applying ReLU: {A.min():.2f} to {A.max():.2f}")

# number of elements deleted
print(f"Total neurons deactivated: {np.sum(A == 0)} out of {A.size}")