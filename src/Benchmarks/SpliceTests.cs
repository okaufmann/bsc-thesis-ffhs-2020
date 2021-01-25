
using BenchmarkDotNet.Attributes;
using System;
using System.Buffers;
using System.Collections.Generic;
using System.Linq;

namespace Thesis2020.Benchmarks
{
    [MemoryDiagnoser]
    [CsvMeasurementsExporter]
    [RPlotExporter]
    public class SpliceTests
    {
        private int[] _testArray;

        [Params(10, 1000, 10000)]
        public int Size { get; set; }

        [GlobalSetup]
        public void Setup()
        {
            _testArray = new int[Size];

            for (var i = 0; i < Size; i++) { 
                _testArray[i] = i;
            }
        }

        [Benchmark(Baseline = true)]
        public int[] Array()
        {
            return _testArray.Skip(Size / 2).Take(Size / 4).ToArray();
        }

        [Benchmark]
        public List<int> List()
        {
            return _testArray.ToList().Skip(Size / 2).Take(Size / 4).ToList();
        }

        [Benchmark]
        public Span<int> Span()
        {
            return _testArray.AsSpan().Slice(Size / 2, Size / 4);
        }

        [Benchmark]
        public Memory<int> Memory() {
            return _testArray.AsMemory().Slice(Size / 2, Size / 4);
        }
    }
}
