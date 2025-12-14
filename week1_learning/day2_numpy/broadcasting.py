import numpy as np
import time

A = np.random.rand(10,3)
start_time = time.time()
mean = np.mean(A, axis=0)
B = A - mean
print(A)
print(B)
print(time.time() - start_time)