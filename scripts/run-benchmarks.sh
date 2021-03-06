#!/usr/bin/env bash
set -e

# ensure entrypoint is root directory
cd "$(dirname "$0")/.."

# enter benchmarks folder
cd src

# cleanup
echo "Cleaning up previous data"
rm -Rf bin
rm -Rf obj
rm -Rf BenchmarkDotNet.Artifacts

# run benchmarks
# https://benchmarkdotnet.org/articles/guides/tool.html#help
echo "Running benchmarks"
dotnet run -c Release -- --runtimes netcoreapp31 --filter Thesis2020.Experiments*

echo "Packaging results"
zip -r BenchmarkDotNet.Artifacts.zip BenchmarkDotNet.Artifacts
rm -Rf ../results/
mkdir -p ../results/
mv BenchmarkDotNet.Artifacts.zip ../results/"$(hostname)-results.zip"