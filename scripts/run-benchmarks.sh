#!/usr/bin/env bash

# ensure entrypoint is root directory
cd "$(dirname "$0")/.."

# enter benchmarks folder
cd src

# cleanup
rm -Rf bin
rm -Rf obj
rm -Rf BenchmarkDotNet.Artifacts

# run benchmarks
# https://benchmarkdotnet.org/articles/guides/tool.html#help
dotnet run -c Release -- --runtimes netcoreapp31 --filter Thesis2020.Benchmarks*

zip -r "results".zip "$1"