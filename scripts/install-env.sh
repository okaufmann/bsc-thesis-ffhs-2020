#!/usr/bin/env bash

# ensure entrypoint is root directory
cd "$(dirname "$0")/.."

# Update system
apt update
apt upgrade

# install .net core SDK
# https://docs.microsoft.com/en-us/dotnet/core/install/linux-debian

# Add .net source
wget https://packages.microsoft.com/config/debian/10/packages-microsoft-prod.deb -O packages-microsoft-prod.deb
dpkg -i packages-microsoft-prod.deb

# install sdk
apt update
apt install -y apt-transport-https
apt update
apt install -y dotnet-sdk-3.1

# Installing R
# https://linuxize.com/post/how-to-install-r-on-debian-10/

apt install dirmngr apt-transport-https ca-certificates software-properties-common gnupg2
apt-key adv --keyserver keys.gnupg.net --recv-key 'E19F5F87128899B192B1A2C2AD5F960A256A04AF'
add-apt-repository 'deb https://cloud.r-project.org/bin/linux/debian buster-cran35/'

apt update
apt install r-base