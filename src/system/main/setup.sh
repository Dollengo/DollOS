#!/bin/bash

# Function to install Python based on distribution
install_python() {
    case $1 in
        "ubuntu"|"debian")
            sudo apt update
            sudo apt install -y python3 python3-pip
            ;;
        "arch")
            sudo pacman -Syu
            sudo pacman -S --noconfirm python python-pip
            ;;
        "fedora")
            sudo dnf install -y python3 python3-pip
            ;;
        "opensuse")
            sudo zypper refresh
            sudo zypper install -y python3 python3-pip
            ;;
        *)
            echo "Unsupported distribution. Please install Python manually."
            exit 1
            ;;
    esac
}

# Prompt user for Linux distribution
echo "Please enter your Linux distribution (ubuntu, debian, arch, fedora, opensuse):"
read distro

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Python not found. Installing Python..."
    install_python $distro
else
    echo "Python is already installed."
fi

# Install Python dependencies
echo "Installing Python dependencies..."
sudo pip3 install datetime psutil rich pandas

# Display package information
echo "Starting..."
echo "Package: DollOS
Version: 2.0
Section: base
Priority: optional
Architecture: all
Depends: python3, python3-pip, python3-datetime, python3-psutil, python3-rich, python3-pandas
Maintainer: Tarcísio <dollengo@outlook.com>
Description: Library for Linux beginners. GitHub: github.com/dollengo/dolloslib
"

# Run the main Python script
python3 DollOS.py
