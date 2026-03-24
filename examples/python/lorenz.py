"""Lorenz attractor — 15 lines of NumPy, one stunning plot."""
import numpy as np
import matplotlib.pyplot as plt

dt, n = 0.01, 10000
sigma, beta, rho = 10, 8/3, 28

xyz = np.zeros((n, 3))
xyz[0] = [0.1, 0, 0]

for i in range(n - 1):
    x, y, z = xyz[i]
    xyz[i+1] = xyz[i] + dt * np.array([
        sigma * (y - x),
        x * (rho - z) - y,
        x * y - beta * z
    ])

# Plot — styled for black slide background
fig = plt.figure(figsize=(10, 8), facecolor="black")
ax = fig.add_subplot(projection="3d", facecolor="black")
ax.scatter(*xyz.T, c=np.arange(n), cmap="plasma", s=0.5, alpha=0.8)
ax.set_axis_off()
ax.view_init(elev=25, azim=130)

plt.savefig("../../images/lorenz.png", dpi=200, facecolor="black",
            bbox_inches="tight", pad_inches=0.1)
plt.show()
