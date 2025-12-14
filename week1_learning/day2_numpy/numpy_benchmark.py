import numpy as np
import time

def benchmark(name, start_time):
    end_time = time.time()
    print(f"   ⏱️  {name}: {end_time - start_time:.5f} sec")

def run_benchmarks():
    N = 5_000_000  # 5 Million points (Big Data!)
    print(f"--- 🏎️ Running NumPy Benchmarks (N={N:,}) ---")

    # 1. GENERATE DATA
    t0 = time.time()
    data = np.random.rand(N)
    benchmark("Data Generation", t0)

    # 2. ELEMENT-WISE MATH (Physics Formula)
    # Task: Calculate y = sin(x) + cos(x) for all 5 million points
    t0 = time.time()
    result = np.sin(data)+np.cos(data)   # <--- YOUR CODE HERE
    benchmark("Trig Calculation", t0)

    # 3. FILTERING (Masking)
    # Task: Select only values where data > 0.8
    t0 = time.time()
    mask =  data > 0.8  # <--- Create a boolean array (True/False)
    filtered = result[mask] # <--- Apply the mask to 'data'
    benchmark("Filtering > 0.8", t0)
    print(f"   (Kept {len(filtered)} particles)")

    # 4. DOT PRODUCT
    # Task: Dot product of data with itself
    t0 = time.time()
    dot_prod = np.dot(result, result) # <--- numpy dot product
    benchmark("Dot Product", t0)

if __name__ == "__main__":
    run_benchmarks()