"""Train a neural network to learn XOR — 12 lines."""
import torch
import torch.nn as nn

X = torch.tensor([[0,0],[0,1],[1,0],[1,1]], dtype=torch.float)
y = torch.tensor([[0],[1],[1],[0]], dtype=torch.float)

model = nn.Sequential(nn.Linear(2, 8), nn.ReLU(), nn.Linear(8, 1), nn.Sigmoid())
opt = torch.optim.Adam(model.parameters(), lr=0.01)

for _ in range(1000):
    loss = nn.functional.binary_cross_entropy(model(X), y)
    opt.zero_grad()
    loss.backward()
    opt.step()

with torch.no_grad():
    print("Predictions:", model(X).round().flatten().tolist())
    print("Expected:   ", y.flatten().tolist())
