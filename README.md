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