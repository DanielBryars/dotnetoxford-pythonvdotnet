"""GPU computing in PyTorch — one word changes everything."""
import torch

a = torch.randn(1000, 1000)
b = torch.randn(1000, 1000)
c = a @ b                        # matrix multiply — CPU

if torch.cuda.is_available():
    a, b = a.cuda(), b.cuda()    # move to GPU
    c = a @ b                    # same operation — now on GPU
    print(f"GPU: {c.device}")
else:
    print("No CUDA GPU available — but the code is identical either way")

print(f"Result shape: {c.shape}")
