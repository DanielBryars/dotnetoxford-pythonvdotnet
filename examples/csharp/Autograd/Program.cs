// Automatic differentiation in TorchSharp
//
// Python (3 lines):
//   x = torch.tensor(3.0, requires_grad=True)
//   y = x**2 + 2*x + 1
//   y.backward()
//   print(x.grad)  # 8.0
//
// C#:

using TorchSharp;

var x = torch.tensor(3.0f, requiresGrad: true);

var y = x.pow(2) + 2 * x + 1;   // y = x² + 2x + 1
y.backward();                     // dy/dx = 2x + 2

Console.WriteLine($"x     = {x.item<float>()}");
Console.WriteLine($"y     = {y.item<float>()}");          // 16
Console.WriteLine($"dy/dx = {x.grad()!.item<float>()}");  // 8  (2·3 + 2)

// Verdict: nearly identical — TorchSharp wraps the same libtorch C++ library.
// But note: x.item<float>() vs x.item(), x.grad() vs x.grad
// Small paper cuts everywhere.
