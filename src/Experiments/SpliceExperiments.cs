namespace Thesis2020.Experiments
{
    using BenchmarkDotNet.Attributes;
    using System;
    using System.Linq;

    [MemoryDiagnoser]
    [CsvMeasurementsExporter]
    [RPlotExporter]
    public class SliceExperiments
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
            return _testArray.Skip(Size / 2).Take(Size / 4).ToArray();
        }

        [Benchmark]
        public Span<int> Span()
        {
            return _testArray.AsSpan().Slice(Size / 2, Size / 4);
        }

        [Benchmark]
        public Span<int> Memory()
        {
            return _testMemory.Span.Slice(Size / 2, Size / 4);
        }
    }
}
