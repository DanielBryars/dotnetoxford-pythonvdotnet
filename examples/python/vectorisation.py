"""Why 'slow' Python is fast — vectorisation benchmark."""
import numpy as np
import time

n = 10_000_000

# Pure Python loop
a = list(range(n))
b = list(range(n))
t0 = time.perf_counter()
c = [a[i] + b[i] for i in range(n)]
loop_ms = (time.perf_counter() - t0) * 1000

# NumPy vectorised
a = np.arange(n)
b = np.arange(n)
t0 = time.perf_counter()
c = a + b
numpy_ms = (time.perf_counter() - t0) * 1000

print(f"Python loop: {loop_ms:>8.1f} ms")
print(f"NumPy:       {numpy_ms:>8.1f} ms")
print(f"Speedup:     {loop_ms / numpy_ms:>8.1f}x")
