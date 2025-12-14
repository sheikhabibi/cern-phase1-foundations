import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.stats import linregress


# 1. DEFINE THE PHYSICS MODEL
def decay_law(t, A, tau, B):
    """Equation: N(t) = A * exp(-t/tau) + Background"""
    return A * np.exp(-t / tau) + B

# 2. GENERATE FAKE EXPERIMENTAL DATA
print("--- 🧪 Simulating Experiment ---")
t_data = np.linspace(0, 10, 40)  # Measure for 10 seconds

# The "True" secret values we want to find:
true_params = [1000, 1.5, 50]    # A=1000, tau=1.5s, B=50
y_perfect = decay_law(t_data, *true_params)
# print(y_perfect)

# Add noise (simulating real-world detector error)
noise = np.random.normal(0, 50, size=len(t_data)) 
y_data = y_perfect + noise

# 3. USE SCIPY TO "FIT" THE DATA
# We give it the function, the x-values, and the noisy y-values.
# p0 is our "initial guess" (Start guessing at A=500, tau=1, B=10)
popt, pcov = curve_fit(decay_law, t_data, y_data, p0=[500, 1.0, 10.0])

A_fit, tau_fit, B_fit = popt
print(f"✅ Recovered Parameters:")
print(f"   A   = {A_fit:.2f} (True: 1000)")
print(f"   tau = {tau_fit:.2f} (True: 1.5)")
print(f"   B   = {B_fit:.2f} (True: 50)")

# Extract the values
A_found, tau_found, B_found = popt

# Calculate the error (uncertainty) from pcov
errors = np.sqrt(np.diag(pcov))
A_error, tau_error, B_error = errors

print("\n--- 🔍 THE FINAL VERDICT ---")
print(f"Variable  | Found Value | Uncertainty (+/-)")
print(f"----------|-------------|------------------")
print(f"A (Start) | {A_found:7.2f}     | +/- {A_error:.2f}")
print(f"tau (Life)| {tau_found:7.2f}     | +/- {tau_error:.2f}")
print(f"B (Backg) | {B_found:7.2f}     | +/- {B_error:.2f}")

# stats analysis
slope, intercept, r_value, p_value, std_err = linregress(t_data, y_data)
print(f"{r_value**2 * 100:.4f}% fit and is the trend real? -> {p_value}" )
# 4. PLOT THE RESULT
plt.figure(figsize=(8, 5))
plt.scatter(t_data, y_data, label="Noisy Data (Detector)", color='red', s=15)
plt.plot(t_data, decay_law(t_data, *popt), label="Scipy Fit", color='blue', linewidth=2)
plt.legend()
plt.title("Curve Fitting: Recovering Physics from Noise")
plt.xlabel("Time (s)")
plt.ylabel("Particle Count")
plt.grid(True, alpha=0.3)
plt.show()