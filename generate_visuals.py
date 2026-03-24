"""Generate visual assets for the presentation slides."""

import matplotlib.pyplot as plt
import numpy as np
import os

os.makedirs("images", exist_ok=True)

# --- Vectorisation benchmark chart ---
sizes = ["1K", "10K", "100K", "1M", "10M"]
loop_times = [0.3, 3.1, 31, 320, 3200]      # ms — pure Python loop
numpy_times = [0.01, 0.02, 0.15, 1.2, 12]   # ms — NumPy vectorised

x = np.arange(len(sizes))
width = 0.35

fig, ax = plt.subplots(figsize=(10, 5))
fig.patch.set_facecolor("#191919")
ax.set_facecolor("#191919")

bars1 = ax.bar(x - width/2, loop_times, width, label="Python loop", color="#e74c3c")
bars2 = ax.bar(x + width/2, numpy_times, width, label="NumPy vectorised", color="#2ecc71")

ax.set_yscale("log")
ax.set_xlabel("Array size", color="white", fontsize=13)
ax.set_ylabel("Time (ms, log scale)", color="white", fontsize=13)
ax.set_title("Python Loop vs NumPy Vectorised", color="white", fontsize=16, pad=15)
ax.set_xticks(x)
ax.set_xticklabels(sizes, color="white", fontsize=12)
ax.tick_params(axis="y", colors="white")
ax.legend(fontsize=12, loc="upper left")
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_color("white")
ax.spines["bottom"].set_color("white")

plt.tight_layout()
plt.savefig("images/vectorisation.png", dpi=150, facecolor=fig.get_facecolor())
plt.close()

print("Generated: images/vectorisation.png")
