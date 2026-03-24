// Train a neural network to learn XOR — TorchSharp edition
//
// Python was 12 lines. Let's see C#...

using TorchSharp;
using static TorchSharp.torch;
using static TorchSharp.torch.nn;

var X = torch.tensor(new float[,] { {0,0}, {0,1}, {1,0}, {1,1} });
var y = torch.tensor(new float[,] { {0}, {1}, {1}, {0} });

var model = Sequential(
    ("fc1", Linear(2, 8)),
    ("relu", ReLU()),
    ("fc2", Linear(8, 1)),
    ("sig", Sigmoid())
);

var opt = torch.optim.Adam(model.parameters(), learningRate: 0.01);

for (int epoch = 0; epoch < 1000; epoch++)
{
    using var prediction = model.forward(X);
    using var loss = functional.binary_cross_entropy(prediction, y);

    opt.zero_grad();
    loss.backward();
    opt.step();
}

using (torch.no_grad())
{
    var result = model.forward(X);
    Console.WriteLine($"Predictions: {result.round().flatten()}");
    Console.WriteLine($"Expected:    {y.flatten()}");
}

// Verdict: it works — TorchSharp is genuinely capable.
// But count the lines. Count the usings. Count the `using var` for disposal.
// Every tensor is an unmanaged resource that needs disposing.
// Python's GC + reference counting handles this invisibly.
//
// The Python version:
//   model = nn.Sequential(nn.Linear(2,8), nn.ReLU(), nn.Linear(8,1), nn.Sigmoid())
//   opt = torch.optim.Adam(model.parameters(), lr=0.01)
//   for _ in range(1000):
//       loss = nn.functional.binary_cross_entropy(model(X), y)
//       opt.zero_grad(); loss.backward(); opt.step()
