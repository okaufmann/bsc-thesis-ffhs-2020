#!/usr/bin/env bash

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
dotnet run -c Release -- --runtimes netcoreapp31 --filter Thesis2020.Benchmarks*

echo "Packaging results"
zip -r BenchmarkDotNet.Artifacts.zip BenchmarkDotNet.Artifacts
mkdir -p ../results/
mv BenchmarkDotNet.Artifacts.zip ../results/"$(hostname)-results.zip"