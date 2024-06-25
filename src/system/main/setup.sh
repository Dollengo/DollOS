#!/bin/bash

if ! command -v python &> /dev/null; then
    echo "Python not found. Intalling Python..."
    sudo apt update
    sudo apt install python3
else
    echo "Python installed."
fi

echo "Installing python dependencies..."
sudo pip install datetime psutil rich pandas

echo "Starting..."
echo "Package: DollOS
Version: 1.3
Section: base
Priority: optional
Architecture: all
Depends: python3, python3-pip, python3-datetime, python3-psutil, python3-rich, python3-pandas
Maintainer: Tarcisio <dollengo@outlook.com>
Description: Library for Linux beginners. GitHub: github.com/dollengo/dolloslib
"
python DollOS.py
