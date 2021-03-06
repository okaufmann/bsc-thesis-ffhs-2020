Bachelor-Thesis (DINF), HS20/21
===

## Install

### Prerequirements

Ensure git is installed:

    git --version

Otherwise install it:

    apt update
    apt install -y git

### Install tools

Just run the following script:

    git clone https://github.com/okaufmann/bsc-thesis-ffhs-2020.git
    cd bsc-thesis-ffhs-2020
    sh scripts/install-env.sh

## Run Benchmarks

**NOTICE:** Be sure you install the needed software first!

    sh scripts/run-benchmarks.sh

## Analysis

Run the following Scripts to generate the used graphs and numbers:

    # install dependencies
    pip3 install -r requirements.txt

    # Prepare data
    python3 analyze/prepare-data.py

    # Generate statistical numbers per datatype
    python3 analyze/percentile_per_datatype.py > results/statistics/percentiles_per_datatype.txt

    # Generate statistical numbers per server
    python3 analyze/percentile_per_computer.py  > results/statistics/percentiles_per_computer.txt

    # run the levene test
    python3 analyze/levene-test.py > results/statistics/cpu-levene-test.txt

    # generate boxplot diagrams
    python3 analyze/graphs-per-group.py


## Dependencies

The following dependencies where used and not developed by Oliver Kaufmann:

- [BenchmarkDotNet v0.12.1](https://github.com/dotnet/BenchmarkDotNet/releases/tag/v0.12.1)
- [.NET Core 3.1](https://dotnet.microsoft.com/download/dotnet/3.1)
- [scipy](https://github.com/scipy/scipy)
- [numpy](https://github.com/numpy/numpy)
- [pandas](https://github.com/pandas-dev/pandas)
- [matplotlib](https://github.com/matplotlib/matplotlib)
- [tabulate](https://github.com/astanin/python-tabulate)
- [python3](https://www.python.org/download/releases/3.0/)