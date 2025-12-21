import numpy as np
import time
import math

def teaser():
    N = 10_000_000  # 10 Million particles
    print(f"--- ⚡ HPC Teaser: Processing {N:,} particles ---")
    
    # Create data
    data_list = list(range(N))
    data_numpy = np.arange(N)

    # 🐌 METHOD 1: The Python Loop (The "Slow" Way)
    print("1. Python For-Loop:   ", end="", flush=True)
    start = time.time()
    result_list = []
    for x in data_list:
        result_list.append(x**2 + 5*x)
    t_loop = time.time() - start
    print(f"{t_loop:.4f} seconds")

    # 🚀 METHOD 2: NumPy Vectorization (The "Fast" Way)
    print("2. NumPy Vectorized:  ", end="", flush=True)
    start = time.time()
    result_numpy = data_numpy**2 + 5*data_numpy
    t_numpy = time.time() - start
    print(f"{t_numpy:.4f} seconds")

    # The Verdict
    speedup = t_loop / t_numpy
    print(f"\n🔥 Speedup Factor: {speedup:.1f}x faster")
    print("---------------------------------------------")

if __name__ == "__main__":
    teaser()