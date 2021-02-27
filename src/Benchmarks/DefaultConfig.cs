using BenchmarkDotNet.Configs;
using BenchmarkDotNet.Diagnosers;
using BenchmarkDotNet.Exporters;
using BenchmarkDotNet.Exporters.Csv;
using BenchmarkDotNet.Jobs;
using System;
using System.Collections.Generic;
using System.Text;

namespace Thesis2020.Benchmarks
{
    class DefaultConfig : ManualConfig
    {
        public DefaultConfig()
        {
            AddJob(Job.Default);
            AddDiagnoser(MemoryDiagnoser.Default);
            AddExporter(CsvMeasurementsExporter.Default, RPlotExporter.Default);
        }

    }
}
