using BenchmarkDotNet.Attributes;
using System.Linq;

namespace MiscDemos
{

    public class NameParser
    {
        public string GetLastName(string fullName)
        {
            var names = fullName.Split(" ");
            var lastName = names.LastOrDefault();
            return lastName ?? string.Empty;
        }
    }

    [MemoryDiagnoser]
    public class NameParserBenchmarks
    {
        private const string FullName = "Steve J Gordon";
        private static readonly NameParser Parser = new NameParser();

        [Benchmark(Baseline = true)]
        public void GetLastName()
        {
            Parser.GetLastName(FullName);
        }
    }
}