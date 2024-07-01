# Made by Dollengo(Tarcísio); github.com/dollengo/dollos

import random
from binrobotdollos import *
from morsildollos import *
from dollpycode import *
from dollnotepad import *
import os # os commands
import sys # sys commands
from rich import print # format messages
import subprocess # open any languages codes
import psutil # kernel
import json # json archives
import shutil # kernel
from datetime import datetime # data/time
import time # timer

STATE_FILE = 'system_state.json'
aliases = {}
desktoparray = ["," for _ in range(16)]
desktoparray[0] = "DollPyCode"
desktoparray[4] = "DollNotePad"
desktoparray[8] = "DollAI"
desktoparray[15] = "Settings"
version = """
░█▀▀▄ ░█▀▀▀█ ░█─── ░█───   ░█▀▀▀█ ░█▀▀▀█   █▀█ ─ █▀▀█ 
░█─░█ ░█──░█ ░█─── ░█───   ░█──░█ ─▀▀▀▄▄   ─▄▀ ▄ █▄▀█ 
░█▄▄▀ ░█▄▄▄█ ░█▄▄█ ░█▄▄█   ░█▄▄▄█ ░█▄▄▄█   █▄▄ █ █▄▄█
"""
current_directory = os.path.dirname(os.path.realpath(__file__))
errorscodes = "Codes -> \n404: Unknown error; 101: IndexError; 102: ValueError; 103: FileNotFoundError; 104: FileExistsError; "

helpcommand = ("""[bold] Commands: [/bold]\n*USE . for any commands.\n\n[italic]
.desktop: Show the Desktop
.help: Show help for using the operating system.
.powershell: Execute the commands of Windows PowerShell.
.exit: Exit the system.
.list: List files.
.read: Read a file.
.write: Write to a file.
.rename: Rename a file.
.mkdir: Create a directory.
.rmdir: Remove a directory.
.delete: Delete a file.
.move: Move a file.
.copy: Copy a file.
.cd: Change directory.
.datetime: Display date and time.
.history: Show history.
.usage: Show usage.
.netstat: Show network statistics.
.ps: Show processes.
.kill: Kill a process.
.touch: Create an empty file.
.cat: Display file content.
.head: Display the head of a file.
.tail: Display the tail of a file.
.du: Display disk usage.
.uptime: Show uptime.
.env: Show environment variables.
.setenv: Set an environment variable.
.unsetenv: Unset an environment variable.
.path: Show the system path.
.addpath: Add a directory to the system path.
.removepath: Remove a directory from the system path.
.ports: List open ports.
.ipconfig: Show IP configuration.
.ping: Ping a host.
.traceroute: Trace the route to a host.
.hostname: Show the hostname.
.arp: Show the ARP table.
.route: Show the routing table.
.systeminfo: Show system information.
.diskpart: Manage disk partitions.
.mount: Mount a device.
.umount: Unmount a device.
.chmod: Change file permissions.
.chown: Change file owner.
.lsusb: List USB devices.
.lspci: List PCI devices.
.dmesg: Display system messages.
.date: Display the date.
.time: Display the time.
.man: Show the manual for a command.
.alias: Create an alias.
.unalias: Remove an alias.
.su: Switch user.
.sudo: Execute a command as another user.
.install: Install a package.
.uninstall: Uninstall a package.
.update: Update packages.
.upgrade: Upgrade packages.
.services: List services.
.start: Start a service.
.stop: Stop a service.
.restart: Restart a service.
.enable: Enable a service.
.disable: Disable a service.
.status: Display service status.
.log: Display service log.
.journal: Show the system journal.
.save: Save the current state.
.load: Load a saved state.
.shutdown: Shutdown the system.
.reboot: Reboot the system.
.ldi: List device informations.
.errors: List errors codes.
.dolley: Create a new text file, with encrypted data.
.opendolley: Read the dolley file.
.savestate: Save the aliases, desktoparray etc.
.loadstate: Load the saved state. (to remove just delete the old state in folder.)

`just type the program name: open the program in desktop

*IF HAVE ANY COMMAND THAT NOT EXIST, DO NOT USE*
[/italic]""")

aliases = {}
command_history = []

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def save_state():
    global current_directory, command_history
    state = {
        "current_directory": current_directory,
        "command_history": command_history
    }
    save_path = os.path.join('saves', STATE_FILE)
    with open(save_path, 'w') as f:
        json.dump(state, f)
    print(f"State saved to {save_path}")

def load_state():
    global current_directory, command_history
    load_path = os.path.join('saves', STATE_FILE)
    if os.path.exists(load_path):
        with open(load_path, 'r') as f:
            state = json.load(f)
            current_directory = state.get("current_directory", os.getcwd())
            command_history = state.get("command_history", [])
        print(f"State loaded from {load_path}")
    else:
        print(f"No saved state found at {load_path}")

def start():
    print("\n[bold] --- Welcome to: --- [/bold]")
    print(""" [bold] [italic]
██████╗░░█████╗░██╗░░░░░██╗░░░░░  ░█████╗░░██████╗
██╔══██╗██╔══██╗██║░░░░░██║░░░░░  ██╔══██╗██╔════╝
██║░░██║██║░░██║██║░░░░░██║░░░░░  ██║░░██║╚█████╗░
██║░░██║██║░░██║██║░░░░░██║░░░░░  ██║░░██║░╚═══██╗
██████╔╝╚█████╔╝███████╗███████╗  ╚█████╔╝██████╔╝
╚═════╝░░╚════╝░╚══════╝╚══════╝  ░╚════╝░╚═════╝░
    [/bold] [/italic]\n""")

def show_help():
    print(helpcommand)

def execute_powershell():
    while True:
        command = input("powershell> ")
        if command.lower() in ['exit', 'quit']:
            break
        result = subprocess.run(["powershell", "-Command", command], capture_output=True, text=True)
        print(result.stdout)
        print(result.stderr)

def exit_system():
    print("Exiting system...")
    exit()

def list_files():
    for item in os.listdir(current_directory):
        print(item)

def read_file(filename):
    try:
        with open(os.path.join(current_directory, filename), 'r') as file:
            print(file.read())
    except FileNotFoundError:
        print(f"File {filename} not found.")

def write_file(filename):
    with open(os.path.join(current_directory, filename), 'w') as file:
        content = input("Enter content: ")
        file.write(content)
        print(f"Written to {filename}")

def rename_file(old_name, new_name):
    os.rename(os.path.join(current_directory, old_name), os.path.join(current_directory, new_name))
    print(f"Renamed {old_name} to {new_name}")

def create_directory(dirname):
    os.makedirs(os.path.join(current_directory, dirname), exist_ok=True)
    print(f"Directory {dirname} created.")

def remove_directory(dirname):
    shutil.rmtree(os.path.join(current_directory, dirname))
    print(f"Directory {dirname} removed.")

def delete_file(filename):
    os.remove(os.path.join(current_directory, filename))
    print(f"File {filename} deleted.")

def move_file(src, dest):
    shutil.move(os.path.join(current_directory, src), os.path.join(current_directory, dest))
    print(f"Moved {src} to {dest}")

def copy_file(src, dest):
    shutil.copy(os.path.join(current_directory, src), os.path.join(current_directory, dest))
    print(f"Copied {src} to {dest}")

def change_directory(dirname):
    global current_directory
    if dirname == "..":
        current_directory = os.path.abspath(os.path.join(current_directory, ".."))
        print(f"Changed directory to {current_directory}")
    elif os.path.isdir(os.path.join(current_directory, dirname)):
        current_directory = os.path.join(current_directory, dirname)
        print(f"Changed directory to {current_directory}")
    else:
        print(f"Directory {dirname} does not exist.")

def display_datetime():
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

def show_history():
    for cmd in command_history:
        print(cmd)

def show_usage():
    cpu_usage = psutil.cpu_percent()
    memory_usage = psutil.virtual_memory().percent
    print(f"CPU Usage: {cpu_usage}%")
    print(f"Memory Usage: {memory_usage}%")

def show_netstat():
    result = subprocess.run(["netstat"], capture_output=True, text=True)
    print(result.stdout)

def show_processes():
    for proc in psutil.process_iter(['pid', 'name']):
        print(proc.info)

def kill_process(pid):
    try:
        p = psutil.Process(pid)
        p.terminate()
        print(f"Process {pid} terminated.")
    except psutil.NoSuchProcess:
        print(f"Process {pid} not found.")

def create_empty_file(filename):
    open(os.path.join(current_directory, filename), 'a').close()
    print(f"Empty file {filename} created.")

def display_file_content(filename):
    read_file(filename)

def display_file_head(filename, n):
    try:
        with open(os.path.join(current_directory, filename), 'r') as file:
            lines = file.readlines()
            for line in lines[:int(n)]:
                print(line, end='')
    except FileNotFoundError:
        print(f"File {filename} not found.")

def display_file_tail(filename, n):
    try:
        with open(os.path.join(current_directory, filename), 'r') as file:
            lines = file.readlines()
            for line in lines[-int(n):]:
                print(line, end='')
    except FileNotFoundError:
        print(f"File {filename} not found.")

def display_disk_usage():
    total, used, free = shutil.disk_usage(current_directory)
    print(f"Total: {total // (2**30)} GiB")
    print(f"Used: {used // (2**30)} GiB")
    print(f"Free: {free // (2**30)} GiB")

def show_uptime():
    uptime = datetime.now() - datetime.fromtimestamp(psutil.boot_time())
    print(f"Uptime: {uptime}")

def show_env():
    for key, value in os.environ.items():
        print(f"{key}={value}")

def set_env(key, value):
    os.environ[key] = value
    print(f"Environment variable {key} set to {value}")

def unset_env(key):
    os.environ.pop(key, None)
    print(f"Environment variable {key} removed")

def show_path():
    print(os.environ.get('PATH'))

def add_path(path):
    os.environ['PATH'] += os.pathsep + path
    print(f"Added {path} to PATH")

def remove_path(path):
    paths = os.environ['PATH'].split(os.pathsep)
    paths.remove(path)
    os.environ['PATH'] = os.pathsep.join(paths)
    print(f"Removed {path} from PATH")

def list_open_ports():
    result = subprocess.run(["netstat", "-an"], capture_output=True, text=True)
    print(result.stdout)

def show_ipconfig():
    result = subprocess.run(["ipconfig"], capture_output=True, text=True)
    print(result.stdout)

def ping_host(host):
    result = subprocess.run(["ping", host], capture_output=True, text=True)
    print(result.stdout)

def traceroute_host(host):
    result = subprocess.run(["tracert", host], capture_output=True, text=True)
    print(result.stdout)

def show_hostname():
    print(os.uname().nodename)

def show_arp():
    result = subprocess.run(["arp", "-a"], capture_output=True, text=True)
    print(result.stdout)

def version_print():
    print(version)

def show_route():
    result = subprocess.run(["route", "print"], capture_output=True, text=True)
    print(result.stdout)

def show_systeminfo():
    result = subprocess.run(["systeminfo"], capture_output=True, text=True)
    print(result.stdout)

def manage_diskpart():
    result = subprocess.run(["diskpart"], capture_output=True, text=True)
    print(result.stdout)

def mount_device(device, path):
    result = subprocess.run(["mount", device, path], capture_output=True, text=True)
    print(result.stdout)

def unmount_device(path):
    result = subprocess.run(["umount", path], capture_output=True, text=True)
    print(result.stdout)

def change_permissions(mode, filename):
    os.chmod(os.path.join(current_directory, filename), int(mode, 8))
    print(f"Changed permissions of {filename} to {mode}")

def change_owner(user_group, filename):
    user, group = user_group.split(':')
    shutil.chown(os.path.join(current_directory, filename), user, group)
    print(f"Changed owner of {filename} to {user}:{group}")

def list_usb():
    result = subprocess.run(["lsusb"], capture_output=True, text=True)
    print(result.stdout)

def list_pci():
    result = subprocess.run(["lspci"], capture_output=True, text=True)
    print(result.stdout)

def display_dmesg():
    result = subprocess.run(["dmesg"], capture_output=True, text=True)
    print(result.stdout)

def display_date():
    print(datetime.now().strftime("%Y-%m-%d"))

def display_time():
    print(datetime.now().strftime("%H:%M:%S"))

def show_man(command):
    result = subprocess.run(["man", command], capture_output=True, text=True)
    print(result.stdout)

def create_alias(name, command):
    aliases[name] = command
    print(f"Alias {name} created for {command}")

def remove_alias(name):
    if name in aliases:
        del aliases[name]
        print(f"Alias {name} removed")
    else:
        print(f"Alias {name} not found")

def print_errors():
    print(errorscodes)

def switch_user(user):
    print(f"Switching to user {user} is not implemented yet.")

def sudo_command(command):
    result = subprocess.run(["sudo"] + command.split(), capture_output=True, text=True)
    print(result.stdout)
    print(result.stderr)

def install_package(package):
    result = subprocess.run(["pip", "install", package], capture_output=True, text=True)
    print(result.stdout)
    print(result.stderr)

def uninstall_package(package):
    result = subprocess.run(["pip", "uninstall", "-y", package], capture_output=True, text=True)
    print(result.stdout)
    print(result.stderr)

def update_packages():
    result = subprocess.run(["pip", "list", "--outdated"], capture_output=True, text=True)
    print(result.stdout)

def upgrade_packages():
    result = subprocess.run(["pip", "install", "--upgrade", "pip"], capture_output=True, text=True)
    print(result.stdout)
    print(result.stderr)

def list_services():
    result = subprocess.run(["sc", "query", "state= all"], capture_output=True, text=True)
    print(result.stdout)

def start_service(service):
    result = subprocess.run(["net", "start", service], capture_output=True, text=True)
    print(result.stdout)
    print(result.stderr)

def stop_service(service):
    result = subprocess.run(["net", "stop", service], capture_output=True, text=True)
    print(result.stdout)
    print(result.stderr)

def restart_service():
    exit()
def enable_service(service):
    result = subprocess.run(["sc", "config", service, "start=", "auto"], capture_output=True, text=True)
    print(result.stdout)
    print(result.stderr)

def disable_service(service):
    result = subprocess.run(["sc", "config", service, "start=", "disabled"], capture_output=True, text=True)
    print(result.stdout)
    print(result.stderr)

def display_service_status(service):
    result = subprocess.run(["sc", "query", service], capture_output=True, text=True)
    print(result.stdout)

def display_service_log(service):
    print(f"Displaying log for {service} is not implemented yet.")

def save_state(filename):
    state = {
        "current_directory": current_directory,
        "command_history": command_history
    }
    with open(filename, 'w') as f:
        json.dump(state, f)
    print(f"State saved to {filename}")

def load_state(filename):
    global current_directory, command_history
    with open(filename, 'r') as f:
        state = json.load(f)
        current_directory = os.path.dirname('system')
        command_history = state.get("command_history", [])
    print(f"State loaded from {filename}")

def whoami():
    print(os.getlogin())

def shutdown_system():
    print("Shutting down...")
    subprocess.run(["shutdown", "/s", "/t", "0"])

def reboot_system():
    print("Rebooting...")
    subprocess.run(["shutdown", "/r", "/t", "0"])

def encrypt(text):
    encrypted_text = ""
    for char in text:
        encrypted_text += chr(ord(char) + 3)  # Simples deslocamento de 3 caracteres na tabela ASCII
    return encrypted_text

# Função de descriptografia
def decrypt(text):
    decrypted_text = ""
    for char in text:
        decrypted_text += chr(ord(char) - 3)  # Reverte o deslocamento de 3 caracteres na tabela ASCII
    return decrypted_text

def writedolley():
    print("Type the text you want. Press Enter twice to finish. Type 'save()' to save or 'exit()' to quit without saving.")
    
    dolleylines = []
    while True:
        dolleyline = input()
        if dolleyline == 'save()':
            dolleyfile_name = input("Enter the file name (without extension): ") + '.dolley'
            save_path = os.path.join(current_directory, "saves", "dolley", dolleyfile_name)
            with open(save_path, 'w') as f:
                for line in dolleylines:
                    encrypted_line = encrypt(line)
                    f.write(encrypted_line + '\n')
            print(f"File '{dolleyfile_name}' saved successfully in 'saves/dolley/'.")
            print(f"Your encrypted text: {[encrypt(line) for line in dolleylines]}")
            main_loop()
        elif dolleyline == 'exit()':
            break
        else:
            dolleylines.append(dolleyline)

def read_dolley():
    dolleyfile_name = input("Enter the file name (without extension): ") + '.dolley'
    try:
        file_path = os.path.join(current_directory, "saves", "dolley", dolleyfile_name)
        with open(file_path, 'r') as f:
            dolleycontent = f.readlines()
            print("File content:")
            for line in dolleycontent:
                print(decrypt(line.strip()))  # Descriptografa cada linha ao imprimir
    except FileNotFoundError:
        print("File not found: " + dolleyfile_name)

def curiosities():
    curiosities = {
        1: "Do you know that, this system was made for a young boy with 14 years old??",
        2: "Do you know that, this system was started made with windows, after v1.1 the creator switch the system for use linux??",
        3: "Do you know that, this system was made for ubuntu servers?? After the v1.0 release, the creator switch for Linux beginners.",
        4: "Do you know that, you can create text files encrypted with the '.dolley' archive?? Open the sudo application '.dolley' to create. And open the sudo application '.opendolley' to open the archives.",
        5: "Do you know that, this system was made with python??",
        6: "I don't know what I write...",
    }
    curiositiesrandom = random.randint(1, len(curiosities))
    print(curiosities[curiositiesrandom])
    main_loop()

def calculator():
    print("Welcome to the calculator!")
    print("What you want?")
    print("1 - Addition")
    print("2 - Subtraction")
    print("3 - Multiplication")
    print("4 - Division")
    print("5 - Exit")
    calculatorcommand = input("-> ")
    if calculatorcommand == "1":
        print("Addition")
        print("Enter the first number: ")
        firstnumber = int(input("-> "))
        print("Enter the second number: ")
        secondnumber = int(input("-> "))
        print(firstnumber + secondnumber)
    elif calculatorcommand == "2":
        print("Subtraction")
        print("Enter the first number: ")
        firstnumber = int(input("-> "))
        print("Enter the second number: ")
        secondnumber = int(input("-> "))
        print(firstnumber - secondnumber)
    elif calculatorcommand == "3":
        print("Multiplication")
        print("Enter the first number: ")
        firstnumber = int(input("-> "))
        print("Enter the second number: ")
        secondnumber = int(input("-> "))
        print(firstnumber * secondnumber)
    elif calculatorcommand == "4":
        try:
            print("Division")
            print("Enter the first number: ")
            firstnumber = int(input("-> "))
            print("Enter the second number: ")
            secondnumber = int(input("-> "))
            print(firstnumber / secondnumber)
        except ZeroDivisionError:
            print("ZERO DIVISION ERROR!")
            print("Error 100; Please read the error codes for about more.")
            main_loop()
    elif calculatorcommand == "5":
        main_loop()
    else:
        print("Error 101; Please read the error codes for about more.")
        main_loop()

def DollAI():
    print("Welcome, i'm DollAI, the artificial intelligence of DollOS!")
    print("What you want?")
    print("1 - Calculator")
    print("2 - Morsil Robot")
    print("3 - Bin Robot")
    print("4 - Curiosities")
    print("5 - Exit")
    dollaicommand = input("-> ")
    if dollaicommand == "1":
        calculator()
    elif dollaicommand == "2":
        runmorsil()
    elif dollaicommand == "3":
        runbinrobot()
    elif dollaicommand == "4":
        curiosities()
    elif dollaicommand == "5":
        show_help()
        main_loop()
    else:
        print("Error 102; Please read the error codes for about more.")
        main_loop()

def handle_command(command):
    global current_directory
    command_history.append(command)
    parts = command.split()
    if not parts:
        return

    cmd = parts[0]
    args = parts[1:]

    if cmd in aliases:
        cmd = aliases[cmd]

    command_map = {
        ".help": show_help,
        ".powershell": execute_powershell,
        ".exit": exit_system,
        ".list": list_files,
        ".read": lambda: read_file(args[0]),
        ".write": lambda: write_file(args[0]),
        ".rename": lambda: rename_file(args[0], args[1]),
        ".mkdir": lambda: create_directory(args[0]),
        ".rmdir": lambda: remove_directory(args[0]),
        ".delete": lambda: delete_file(args[0]),
        ".move": lambda: move_file(args[0], args[1]),
        ".copy": lambda: copy_file(args[0], args[1]),
        ".cd": lambda: change_directory(args[0]),
        ".datetime": display_datetime,
        ".history": show_history,
        ".usage": show_usage,
        ".netstat": show_netstat,
        ".ps": show_processes,
        ".kill": lambda: kill_process(int(args[0])),
        ".touch": lambda: create_empty_file(args[0]),
        ".cat": lambda: display_file_content(args[0]),
        ".head": lambda: display_file_head(args[0], args[1]),
        ".tail": lambda: display_file_tail(args[0], args[1]),
        ".du": display_disk_usage,
        ".uptime": show_uptime,
        ".env": show_env,
        ".setenv": lambda: set_env(args[0], args[1]),
        ".unsetenv": lambda: unset_env(args[0]),
        ".path": show_path,
        ".addpath": lambda: add_path(args[0]),
        ".removepath": lambda: remove_path(args[0]),
        ".ports": list_open_ports,
        ".ipconfig": show_ipconfig,
        ".ping": lambda: ping_host(args[0]),
        ".traceroute": lambda: traceroute_host(args[0]),
        ".hostname": show_hostname,
        ".arp": show_arp,
        ".route": show_route,
        ".systeminfo": show_systeminfo,
        ".diskpart": manage_diskpart,
        ".mount": lambda: mount_device(args[0], args[1]),
        ".umount": lambda: unmount_device(args[0]),
        ".chmod": lambda: change_permissions(args[0], args[1]),
        ".chown": lambda: change_owner(args[0], args[1]),
        ".lsusb": list_usb,
        ".lspci": list_pci,
        ".dmesg": display_dmesg,
        ".date": display_date,
        ".time": display_time,
        ".man": lambda: show_man(args[0]),
        ".alias": lambda: create_alias(args[0], args[1]),
        ".unalias": lambda: remove_alias(args[0]),
        ".su": lambda: switch_user(args[0]),
        ".sudo": lambda: sudo_command(" ".join(args)),
        ".install": lambda: install_package(args[0]),
        ".uninstall": lambda: uninstall_package(args[0]),
        ".update": update_packages,
        ".upgrade": upgrade_packages,
        ".services": list_services,
        ".start": lambda: start_service(args[0]),
        ".stop": lambda: stop_service(args[0]),
        ".restart": restart_service,
        ".enable": lambda: enable_service(args[0]),
        ".disable": lambda: disable_service(args[0]),
        ".status": lambda: display_service_status(args[0]),
        ".log": lambda: display_service_log(args[0]),
        ".save": lambda: save_state(args[0]),
        ".load": lambda: load_state(args[0]),
        ".shutdown": shutdown_system,
        ".reboot": reboot_system,
        ".desktop": desktop,
        "dollpycode": dollpycode,
        "dollnotepad": dollnotepad,
        ".ldi": list_device_info,
        ".clear": clear_console,
        ".start": start,
        ".error": print_errors,
        ".dolley": writedolley,
        ".opendolley": read_dolley,
        "settings": settings,
        ".savestate": save_state,
        ".loadstate": load_state,
        ".version": version_print,
        "dollai": DollAI,
    }

    if cmd in command_map:
        command_map[cmd]()
    else:
        print(f"Unknown command: {cmd}")

def list_device_info():
    for device in psutil.disk_partitions():
        print(f"Device: {device.device}, Mountpoint: {device.mountpoint}, File system type: {device.fstype}")

def desktop():
    print(f" {desktoparray[0]}  |  {desktoparray[1]}  |  {desktoparray[2]}  |  {desktoparray[3]}")
    print(f" {desktoparray[4]}  |  {desktoparray[5]}  |  {desktoparray[6]}  |  {desktoparray[7]}")
    print(f" {desktoparray[8]}  |  {desktoparray[9]}  |  {desktoparray[10]}  |  {desktoparray[11]}")
    print(f" {desktoparray[12]}  |  {desktoparray[13]}  |  {desktoparray[14]}  |  {desktoparray[15]}")

def settings():
    print("Settings:")
    print("1 - Change icon desktop.")
    print("2 - Remove icon desktop.")
    print("3 - About")
    print("4 - Quit")
    dolleysettings = input("Choose an option: ")
    
    if dolleysettings == "1":
        print("Change icon desktop: ")
        print("Choose the icon index [0 - 15]: ")
        dolleysettingsicon = int(input())
        if 0 <= dolleysettingsicon < 16:
            new_icon_path = input("Enter the new icon path (separated by '\\\\'): ")
            if not new_icon_path.endswith('.py'):
                print("Error: Only .py files are allowed.")
                return
            
            if not os.path.isfile(new_icon_path):
                print("Error: File not found.")
                return
            
            desktoparray[dolleysettingsicon] = new_icon_path
            print(f"Icon at index {dolleysettingsicon} changed to {new_icon_path}")
        else:
            print("Invalid index. Please choose a number between 0 and 15.")

    elif dolleysettings == "2":
        print("Remove icon desktop: ")
        print("Choose the icon index [0 - 15]: ")
        dolleysettingsicon = int(input())
        if 0 <= dolleysettingsicon < 16:
            if desktoparray[dolleysettingsicon] != ",":
                desktoparray[dolleysettingsicon] = ","
                print(f"Icon at index {dolleysettingsicon} removed.")
            else:
                print("No icon at this index to remove.")
        else:
            print("Invalid index. Please choose a number between 0 and 15.")

    elif dolleysettings == "3":
        print("About: This is a desktop icon manager.")

    elif dolleysettings == "4":
        print("Quitting settings.")
    
    else:
        print("Invalid option. Please choose between 1 and 4.")

# Main loop
def main_loop():
    try:
        while True:
            command = input(f"{os.getlogin()}@{os.uname().nodename} ~ {current_directory}: ").lower()
            handle_command(command)
    except (IndexError):
        print("Error 101")
        main_loop()
    except (ValueError):
        print("Error 102")
        main_loop()
    except (FileExistsError):
        print("Error 104")
        main_loop()
    except (FileNotFoundError):
        print("Error 103")
        main_loop()

if __name__ == "__main__":
    start()
    main_loop()


# Made by Dollengo(Tarcísio); github.com/dollengo/dollos
