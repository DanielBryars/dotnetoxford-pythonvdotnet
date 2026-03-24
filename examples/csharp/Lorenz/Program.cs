// Lorenz attractor in C# — same maths, more ceremony
const double dt = 0.01;
const int n = 10000;
const double sigma = 10, beta = 8.0 / 3, rho = 28;

var x = new double[n];
var y = new double[n];
var z = new double[n];
x[0] = 0.1;

for (int i = 0; i < n - 1; i++)
{
    x[i + 1] = x[i] + dt * sigma * (y[i] - x[i]);
    y[i + 1] = y[i] + dt * (x[i] * (rho - z[i]) - y[i]);
    z[i + 1] = z[i] + dt * (x[i] * y[i] - beta * z[i]);
}

// Computation done. But now what?
// No built-in 3D scatter plot.
// Options: ScottPlot (2D only), OxyPlot, export CSV and plot elsewhere.
// In Python this was one line: ax.scatter(*xyz.T, ...)

Console.WriteLine($"Computed {n} Lorenz points.");
Console.WriteLine($"First: ({x[0]:F2}, {y[0]:F2}, {z[0]:F2})");
Console.WriteLine($"Last:  ({x[n-1]:F2}, {y[n-1]:F2}, {z[n-1]:F2})");
Console.WriteLine();
Console.WriteLine("// To plot this, you'd need to:");
Console.WriteLine("//   1. Pick a plotting library (ScottPlot? OxyPlot? LiveCharts?)");
Console.WriteLine("//   2. Add the NuGet package");
Console.WriteLine("//   3. Write 20+ lines of plotting code");
Console.WriteLine("//   4. Realise none of them do 3D scatter well");
Console.WriteLine("//   5. Export to CSV and open in Python anyway");
