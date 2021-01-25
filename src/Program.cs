using BenchmarkDotNet.Running;
using System;
using System.Runtime.InteropServices;
using Thesis2020.Benchmarks;

namespace Thesis2020
{
    class Program
    {
        static void Main(string[] args)
        {
            BenchmarkSwitcher.FromAssembly(typeof(Program).Assembly).Run(args);
        }
    }
}
