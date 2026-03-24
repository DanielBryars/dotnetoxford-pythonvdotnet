"""Automatic differentiation — calculus for free."""
import torch

x = torch.tensor(3.0, requires_grad=True)

y = x**2 + 2*x + 1   # y = x² + 2x + 1
y.backward()           # dy/dx = 2x + 2

print(f"x = {x.item()}")
print(f"y = {y.item()}")        # 16
print(f"dy/dx = {x.grad.item()}")  # 8  (2·3 + 2)
