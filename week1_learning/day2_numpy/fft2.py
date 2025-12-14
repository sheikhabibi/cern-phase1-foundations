import numpy as np
import matplotlib.pyplot as plt

def explain_fftfreq():
    # 1. Setup: 10 samples, taken 0.1 seconds apart
    N = 10          # Number of dots
    dt = 0.1        # 0.1 seconds between dots (Sample Rate = 10Hz)
    
    # 2. Ask NumPy for the frequencies
    freqs = np.fft.fftfreq(n=N, d=dt)
    
    print("--- The Raw Output of fftfreq ---")
    print(f"Indices: {list(range(N))}")
    print(f"Freqs:   {freqs}")
    print("---------------------------------")
    
    # 3. Why Negative Frequencies? 
    # Mathematical symmetry. For real-world physics, we often ignore them 
    # or use np.fft.rfftfreq (Real FFT) which only gives positives.

    # 4. Plot to visualize
    plt.figure(figsize=(8, 4))
    x = np.fft.fftfreq(len(freqs), d=dt)
    y = np.abs(np.fft.fft(freqs))
    plt.plot(x, y)
    plt.stem(freqs, np.ones_like(freqs)) # Just plotting stems at the freq locations
    plt.title(f"Visualizing fftfreq(n={N}, d={dt})")
    plt.xlabel("Frequency (Hz)")
    plt.grid(True)
    plt.axvline(0, color='k')
    plt.show()

if __name__ == "__main__":
    explain_fftfreq()