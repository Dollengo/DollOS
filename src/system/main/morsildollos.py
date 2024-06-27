# Dictionary to convert ASCII characters to Morse code
codes = {
    "a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.",
    "g": "--.", "h": "....", "i": "..", "j": ".---", "k": "-.-", "l": ".-..",
    "m": "--", "n": "-.", "o": "---", "p": ".--.", "q": "--.-", "r": ".-.",
    "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--", "x": "-..-",
    "y": "-.--", "z": "--..", "1": ".----", "2": "..---", "3": "...--",
    "4": "....-", "5": ".....", "6": "-....", "7": "--...", "8": "---..",
    "9": "----.", "0": "-----", " ": "/", ".": ".-.-.-", "?": "..--..",
    "!": "-.-.--", ",": "--..--", "=": "-...-", "/": "-..-.", "-": "-....-",
    "+": ".-.-.", ":": "---...", ";": "-.-.-.", "'": ".----.", "(": "-.--.",
    ")": "-.--.-", "&": ".-..."
}

# Invert the dictionary to get Morse to ASCII mapping
codes_reversed = {value: key for key, value in codes.items()}

# Function to run the main program
def runmorsil():
    print("Morsil: Hello, I'm Morsil, a robot FLUENT in Morse code.")

    while True:
        print("Morsil: Type '1' for (morse -> ascii), '2' for (ascii -> morse) or 'esc' for exit: ")
        chose = input().lower()

        if chose == '1':
            # Morse to ASCII conversion
            morse = input("Morsil: Type the Morse code to be converted (separate each letter with a space): ")
            ascii = ''.join(codes_reversed.get(i, '?') for i in morse.split(' '))
            print(f"Morsil: {ascii}")
        elif chose == '2':
            # ASCII to Morse conversion
            ascii = input("Morsil: Type the text to be converted: ").lower()
            morse = ' '.join(codes.get(i, '/ ') for i in ascii)
            print(f"Morsil: {morse}")
        elif chose == "esc":
            # Exit the program
            print("Morsil: Bye...")
            break
        else:
            # Display an error message if the input is invalid
            print("Morsil: Invalid input. Type '1', '2', or 'esc'.")

# Execute a função run() se o script for executado diretamente
if __name__ == "__main__":
    runmorsil()
