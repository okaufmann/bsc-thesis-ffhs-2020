
using BenchmarkDotNet.Attributes;
using System;
using System.Collections.Generic;
using System.Linq;

namespace Thesis2020.Benchmarks
{
    [MemoryDiagnoser]
    [CsvMeasurementsExporter]
    [RPlotExporter]
    public class SplicePreparedMemoryTests
    {
        private int[] _testArray;
        private List<int> _testList;
        private Memory<int> _testMemory;

        [Params(10, 1000, 10000)]
        public int Size { get; set; }

        [GlobalSetup]
        public void Setup()
        {
            _testArray = new int[Size];

            for (var i = 0; i < Size; i++) { 
                _testArray[i] = i;
            }

           _testList = _testArray.ToList();
           _testMemory = _testArray.AsMemory();
        }

        [Benchmark(Baseline = true)]
        public Span<int> Span()
        {
            return _testArray.AsSpan().Slice(Size / 2, Size / 4);
        }

        [Benchmark]
        public Memory<int> Memory() {
            return _testMemory.Slice(Size / 2, Size / 4);
        }
    }
}
