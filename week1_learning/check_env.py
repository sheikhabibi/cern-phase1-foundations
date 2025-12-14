import numpy as np
import torch
import time
import sys

def benchmark_test():
    print(f"--- 🚀 CERN Prep Environment Check (Python {sys.version.split()[0]}) ---")
    
    # 1. Test NumPy (Matrix Multiplication)
    N = 2000
    print(f"Testing NumPy {np.__version__} with {N}x{N} matrix multiply...", end="")
    start = time.time()
    A = np.random.rand(N, N)
    B = np.random.rand(N, N)
    C = np.dot(A, B)
    duration = time.time() - start
    print(f" Done! ({duration:.4f}s)")

    # 2. Test PyTorch (Tensors)
    print(f"Testing PyTorch {torch.__version__}...", end="")
    x = torch.rand(5, 3)
    print(" Done!")
    
    # 3. Check GPU
    if torch.cuda.is_available():
        print(f"✅ CUDA is available! (Device: {torch.cuda.get_device_name(0)})")
    else:
        print("⚠️ CUDA not detected (Running on CPU). This is fine for Week 1.")

    print("\n✅ SYSTEM READY. Day 1 Complete.")

if __name__ == "__main__":
    benchmark_test()