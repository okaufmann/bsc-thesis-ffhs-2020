#!/usr/bin/env bash

# Update system
apt update
apt upgrade

# Add .net source
wget https://packages.microsoft.com/config/debian/10/packages-microsoft-prod.deb -O packages-microsoft-prod.deb
dpkg -i packages-microsoft-prod.deb

# install .net core SDK
apt update
apt install -y apt-transport-https
apt update
apt install -y dotnet-sdk-3.1

# install Benchmark DotNet
dotnet tool install -g BenchmarkDotNet.Tool