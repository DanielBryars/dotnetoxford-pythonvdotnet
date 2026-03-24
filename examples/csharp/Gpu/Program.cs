// GPU computing in TorchSharp
// Python:  a.cuda()
// C#:      a.cuda()  — actually identical here, TorchSharp mirrors the API
//
// But you need:
//   1. The right NuGet package (libtorch-cpu vs libtorch-cuda)
//   2. The right native runtime (~800MB download)
//   3. Matching CUDA toolkit version

using TorchSharp;

var a = torch.randn(1000, 1000);
var b = torch.randn(1000, 1000);
var c = a.mm(b);                     // matrix multiply — CPU

if (torch.cuda_is_available())
{
    a = a.cuda();
    b = b.cuda();
    c = a.mm(b);                     // same operation — GPU
    Console.WriteLine($"GPU: {c.device}");
}
else
{
    Console.WriteLine("No CUDA GPU available (using CPU backend)");
}

Console.WriteLine($"Result shape: [{c.shape[0]}, {c.shape[1]}]");

// Verdict: TorchSharp mirrors PyTorch well here.
// The friction isn't the code — it's the 800MB native dependency
// and figuring out which NuGet package matches your CUDA version.
