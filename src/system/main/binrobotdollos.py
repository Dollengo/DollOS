import time

# Converts an ASCII string to binary
def str_to_bin(string):
    # Converts each character to its corresponding 8-bit binary value
    return ' '.join(format(ord(char), '08b') for char in string.replace('_', ' '))

# Converts a binary string (space-separated) to ASCII
def bin_to_str(binary):
    # Converts each binary byte back to its corresponding ASCII character
    string = ''.join(chr(int(b, 2)) for b in binary.split(' '))
    return string.replace(' ', '_')

# Function to run the main program
def runbinrobot():
    print("Bin: Hello, I am Bin, a robot FLUENT in binary code.")
    time.sleep(1)

    while True:
        print("Bin: Type '1' for (ASCII -> binary), '2' for (binary -> ASCII) or 'esc' to exit: ")
        user = input().lower().strip()

        if user == "esc":
            print("Bin: Exiting...")
            break
        elif user == "1":
            print("Bin: Enter an ASCII string: ")
            string = input()
            print(f"Bin: {str_to_bin(string)}")
        elif user == "2":
            print("Bin: Enter a binary code (separate bytes with spaces): ")
            binary = input()
            if all(bit in ('0', '1') for bit in binary.replace(' ', '')):
                print(f"Bin: {bin_to_str(binary)}")
            else:
                print("Bin: Invalid binary code. Ensure it contains only '0' or '1'.")
        else:
            print("Bin: Invalid input. Type '1', '2', or 'esc'.")

# Execute a função run() se o script for executado diretamente
if __name__ == "__main__":
    runbinrobot()
