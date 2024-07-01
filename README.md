***

![Captura de tela de 2024-06-20 21-12-08](https://github.com/Dollengo/DollOS/assets/131563888/6225c3fc-7578-459f-96ef-212ad281bc39)

<h1 align="center">DollOS</h1>
<h3 align="center">Software for Linux beginners.</h3>

<p align='center'>
 <a href="https://ko-fi.com/dollengo">
    <img src="https://img.shields.io/badge/sponsor-30363D?style=for-the-badge&logo=GitHub-Sponsors&logoColor=#white" />
  </a>&nbsp;&nbsp;
  <a href="#">
  <img alt="GitHub Repo stars" src="https://img.shields.io/github/stars/dollengo/dollos?style=for-the-badge">
</a>&nbsp;&nbsp;
</p>

[![Latest Release](https://img.shields.io/badge/RELEASE-v2.1-green)][Download]
[![Support](https://img.shields.io/badge/Patreon-Support_Me-orange.svg?logo=Patreon)][Patreon]

***

- **Attention: the source code don't have all archives because GitHub not agree import large archives, so, if you want download the rary, download the [release version](https://github.com/Dollengo/DollOS/releases/tag/DollOS).**

- Resume: It's a software to support you to use linux, if you is an beginner in Linux OS, just use.

- This software, developed by Tarcísio (dollengo), is intended for server management or to provide a user-friendly interface for console users. It's designed to be adaptable for constant updates by users and is licensed under the **MIT License**. It can be utilized on any type of computer operating system.

- The [**main file**](./src/system/main/DollOS.py)

## Overview


| Version |  Download  |
|---------|-------------|
|  v2.1   |  Available   |
|  v2.0   |  Available   |
|  v1.3   |  Available   |
|  v1.2   |  Available   |
|  v1.1   |  N-Available |
|  v1.0   |  N-Available |


This Python software offers a comprehensive set of commands and functionalities to manage server operations efficiently. Whether you need to manipulate files, execute system commands, monitor processes, or manage services, this software provides a versatile solution.

## Features

### Basic Commands

- **File Management**: Manipulate files and directories with commands like `.list`, `.read`, `.write`, `.rename`, `.mkdir`, `.rmdir`, `.delete`, `.move`, and `.copy`.
- **Navigation**: Change directories with `.cd`.
- **System Information**: Retrieve system information such as date and time, environment variables, network statistics, and more using commands like `.datetime`, `.env`, `.netstat`, `.diskpart`, etc.
- **Process Management**: Monitor and manage processes with `.ps`, `.kill`, and other related commands.
- **Service Management**: Control system services with commands like `.start`, `.stop`, `.restart`, `.enable`, `.disable`, and `.status`.
- **Package Management**: Install, uninstall, update, and upgrade packages with `.install`, `.uninstall`, `.update`, and `.upgrade`.
- **Alias Creation**: Create and manage custom command aliases with `.alias` and `.unalias`.

### Additional Functionality

- **Desktop Display**: Visualize available programs on the desktop with the `.desktop` command.
- **PowerShell Execution**: Execute Windows PowerShell commands with `.powershell`.
- **State Management**: Save and load the current system state with `.save` and `.load`.
- **System Shutdown/Reboot**: Perform system shutdown or reboot with `.shutdown` and `.reboot`.

### User-Friendly Interface

The software offers a user-friendly interface with clear commands and rich formatting of messages using the `rich` software.

## Usage

To use any command, simply type it in the console prompt. For commands that require additional arguments, follow the specified syntax.
For apps in desktop use only the name.
- The desktop apps:
    - DollPyCode: A simple IDE to programming your apps.
    - DollNotePad: A simple Notepad to save your notes.
    - DollAI: A assistant to support you quickly.
    - Settings: Just settings, configurations.

Example:
- .list
- .read example.txt
- .write newfile.txt
- .rename oldname.txt newname.txt
- .mkdir newdir
- .rmdir existingdir
- .delete file.txt
- .move oldfile.txt newdir
- .copy oldfile.txt newfile.txt
- .cd directory
- .datetime
- .history
- .usage
-[etc...]

Please note that some commands may not be available or fully implemented, as indicated in the help text.

## Installation

To use this software, simply clone the repository and import the relevant modules into your Python script. Make sure to install any dependencies listed in the `deb-description.txt` file. After this, start the `setup.sh` or ```bash  python DollOS.py```.

## Contribution

Contributions to this software are welcome. Feel free to fork the repository, make improvements, and submit pull requests. Please adhere to the code style and documentation conventions.

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for more details.

## Acknowledgements

Special thanks to Dollengo (Tarcísio) for developing and maintaining this software.

# --------------> READ THE WIKI, THAT YOU WILL FOUND MORE INFORMATIONS FROM THE SOFTWARE!!! <--------------
## [**About more**](https://github.com/Dollengo/DollOS/wiki)

[Download]: (https://github.com/Dollengo/DollOS/releases/tag/DollOS)
[Patreon]: (https://www.patreon.com/collection/608791)
