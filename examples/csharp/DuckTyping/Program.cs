using System.Numerics;

// The Python version:
//   def f(x): return x*x + 2*x
//
// Works on: int, float, complex, ndarray, tensor
// Zero changes needed.

// The C# version — Generic Math (.NET 7+)
T F<T>(T x) where T : INumber<T>
{
    var two = T.One + T.One;
    return x * x + two * x;
}

Console.WriteLine($"int:     {F(3)}");       // 15
Console.WriteLine($"double:  {F(2.5)}");     // 11.25
Console.WriteLine($"decimal: {F(2.5m)}");    // 11.25

// Complex? Won't compile — Complex doesn't implement INumber<T>
// var c = F(new Complex(1, 2));  // <-- error CS0311

// Array? Completely different code needed
var arr = new[] { 1, 2, 3 };
var result = arr.Select(x => F(x)).ToArray();
Console.WriteLine($"array:   [{string.Join(", ", result)}]");  // [3, 8, 15]
// But that's LINQ on each element — not vectorised like NumPy

// GPU tensor? Different universe entirely
// TorchSharp has its own Tensor type with its own API
// torch.tensor([1, 2, 3]).pow(2) + 2 * torch.tensor([1, 2, 3])

Console.WriteLine();
Console.WriteLine("// Python: 1 function, 5 types, 0 changes");
Console.WriteLine("// C#:     1 function, 3 types, and arrays/complex/tensors need separate code");
