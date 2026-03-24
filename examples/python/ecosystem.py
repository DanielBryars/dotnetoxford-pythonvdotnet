"""Python's ecosystem convergence — everyone speaks NumPy."""
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Generate a noisy signal
t = np.linspace(0, 1, 1000)
clean = np.sin(2 * np.pi * 5 * t) + 0.5 * np.sin(2 * np.pi * 12 * t)
noisy = clean + 0.8 * np.random.randn(len(t))

# Filter it — scipy takes NumPy arrays, returns NumPy arrays
b, a = signal.butter(4, 15, fs=1000)
filtered = signal.filtfilt(b, a, noisy)

# Plot it — matplotlib takes NumPy arrays directly
fig, axes = plt.subplots(3, 1, figsize=(10, 6), facecolor="black")
for ax in axes:
    ax.set_facecolor("black")
    ax.tick_params(colors="white")
    for spine in ax.spines.values():
        spine.set_color("#333")

axes[0].plot(t, clean, color="#2ecc71", linewidth=0.8)
axes[0].set_title("Original", color="white")
axes[1].plot(t, noisy, color="#e74c3c", linewidth=0.5, alpha=0.7)
axes[1].set_title("Noisy", color="white")
axes[2].plot(t, filtered, color="#3498db", linewidth=0.8)
axes[2].set_title("Filtered (SciPy Butterworth)", color="white")

plt.tight_layout()
plt.savefig("../../images/ecosystem.png", dpi=150, facecolor="black")
plt.show()
