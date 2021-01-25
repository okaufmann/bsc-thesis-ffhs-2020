#!/usr/bin/env bash

# Update system
sudo apt-get update
sudo apt-get upgrade

# Add .net source
wget https://packages.microsoft.com/config/debian/10/packages-microsoft-prod.deb -O packages-microsoft-prod.deb
sudo dpkg -i packages-microsoft-prod.deb

# install .net core SDK
sudo apt-get update; \
  sudo apt-get install -y apt-transport-https && \
  sudo apt-get update && \
  sudo apt-get install -y dotnet-sdk-3.1

# install Benchmark DotNet
sudo dotnet tool install -g BenchmarkDotNet.Tool