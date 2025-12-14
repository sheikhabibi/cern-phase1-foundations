import numpy as np
import matplotlib.pyplot as plt

# 1. Create a signal
t = np.linspace(0, 1, 400, endpoint=False)
print(len(t))
signal = np.sin(2 * np.pi * 50 * t) + np.sin(2 * np.pi * 80 * t) # 50Hz and 80Hz tones

# 2. Run FFT (The Prism)
frequencies = np.fft.fftfreq(len(t), d=t[1]-t[0])
spectrum = np.fft.fft(signal)

# 3. The result is a spike at 50 and 80!
print("FFT reveals the hidden ingredients of the wave.")

freq = frequencies >= 0     # array of true false
plt.plot(t,signal)
# plt.plot(frequencies[freq],np.abs(spectrum[freq]))
plt.show()