# DollOS - User Guide

## Overview

DollOS is a simplified operating system designed for learning and practicing Linux commands. It provides a command-line interface (CLI) environment similar to Linux, allowing users to execute various commands and perform basic system operations.

# 

## Usage

To use DollOS, follow these steps:

1. **Starting DollOS:**
   - DollOS is launched from the command line using Python.

     ```bash
     python DollOS.py
     ```
     or
     `open setup.sh`

2. **Commands:**
   
   - DollOS supports a variety of commands that mimic Linux terminal commands. Here are some examples:
   
     - `.help`: Display a list of available commands.
     - `.exit`: Exit the DollOS environment.
     - `.list`: List files and directories in the current directory.
     - `.read <file>`: Display the content of a file.
     - `.write <file>`: Write content to a file.
     - `.rename <old> <new>`: Rename a file.
     - `.mkdir <name>`: Create a new directory.
     - `.rmdir <directory>`: Remove a directory.
     - `.delete <file>`: Delete a file.
     - `.move <source> <destination>`: Move a file.
     - `.copy <source> <destination>`: Copy a file.
     - `.cd <directory>`: Change current directory.
     - `.desktop`: Display a desktop with fictitious shortcuts.
     - [etc...]
   
3. **System Information:**
   - DollOS provides commands to retrieve system information:
     
     - `.datetime`: Display current date and time.
     - `.uptime`: Show system uptime.
     - `.usage`: Display CPU and memory usage.
     - `.netstat`: Show network statistics.
     - `.ps`: List all running processes.
     - `.kill <PID>`: Kill a process by its ID.
     - `.env`: Show environment variables.
     - `.setenv <key> <value>`: Set an environment variable.
     - `.unsetenv <key>`: Unset an environment variable.
     - [etc...]

4. **Creating Desktop Shortcuts:**
   - Users can create desktop shortcuts using the `.desktop` command. This command displays a visual representation of shortcuts for programs or tasks.

5. **Additional Functionality:**
   - DollOS includes functionalities for managing files, directories, system processes, and environment variables. Users can explore and practice various Linux-like operations within this simulated environment.

6. **Report:**
    - Any bug or any incompatibility with any Linux dist. Report in `https://github.com/Dollengo/DollOS/issues`.
    - Generally, all bugs or imcompatibility issues only have in Windows.

    - OS approved:
        - Linux:
            - Arch:
                - Arch: 2024.06.01
            - openSUSE:
                - openSUSE: 15.6
            - Fedora:
                - Fedora: 40
            - Ubuntu:
                - Ubuntu: 24.04
                - Ubuntu: 22
            - Debian:
                - Debian: 12.5
        - Windows:
            - Windows: 11
            - Windows: 10
        - MacOS:
            - MacOS: NOT SUPPORTED

## Development Information

- **Language:** DollOS is developed in Python.
- **Libraries Used:** It utilizes libraries such as `datetime`, `psutil`, `rich`, and `pandas` for various functionalities.
- **Maintainer:** DollOS is maintained by Tarcisio <dollengo@outlook.com>.
- **Source:** The source code and additional information can be found at [GitHub - DollOS](https://github.com/dollengo/dollos).

## Feedback and Contributions

Your feedback and contributions to DollOS are welcome! If you encounter any issues, have suggestions, or want to contribute to its development, please visit the GitHub repository or contact the maintainer directly.

Happy exploring with DollOS!
Thank-you for read until here!! <3
