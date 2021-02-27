
namespace Thesis2020.Experiments
{
    using System;
    using System.Linq;
    using BenchmarkDotNet.Attributes;

    [MemoryDiagnoser]
    [CsvMeasurementsExporter]
    [RPlotExporter]
    public class ReverseExperiments
    {
        private int[] _testArray;

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

            _testMemory = _testArray.AsMemory();
        }

        [Benchmark(Baseline = true)]
        public int[] Array()
        {
            return _testArray.Reverse().ToArray();
        }

        [Benchmark]
        public Span<int> Span()
        {
            var span = _testArray.AsSpan();
            span.Reverse();

            return span;
        }

        [Benchmark]
        public Memory<int> Memory()
        {
            _testMemory.Span.Reverse();

            return _testMemory;
        }
    }
}
