
using BenchmarkDotNet.Attributes;
using System;
using System.Buffers;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Thesis2020.Benchmarks.Benchmarks
{
    [MemoryDiagnoser]
    [CsvMeasurementsExporter]
    [RPlotExporter]
    public class ReverseTests
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

            for (var i = 0; i < Size; i++)
            {
                _testArray[i] = i;
            }

            _testList = _testArray.ToList();
            _testMemory = _testArray.AsMemory();
        }

        [Benchmark(Baseline = true)]
        public int[] Array()
        {
            return _testArray.Reverse().ToArray();
        }

        [Benchmark]
        public List<int> List()
        {
             _testList.Reverse();

            return _testList;
        }

        [Benchmark]
        public Span<int> Span()
        {
            var reversed = _testArray.AsSpan();
            reversed.Reverse();

            return reversed;
        }

        //[Benchmark]
        //public Memory<int> Memory()
        //{
        //    // does not exist
        //    return _testMemory.Reverse();
        //}
    }
}
