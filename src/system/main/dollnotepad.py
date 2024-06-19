import os

def dollnotepad():
    notes = []
    print("Welcome to DollNotePad! (type 'exit' to exit or 'save' to save the notes)")
    user_input = ""
    
    current_directory = os.path.dirname(os.path.abspath(__file__))
    notes_directory = "saves\\notes"
    
    if not os.path.exists(os.path.join(current_directory, notes_directory)):
        os.makedirs(os.path.join(current_directory, notes_directory))
    print("----------")
    
    while user_input != "exit":
        user_input = input("")
        if user_input == "save":
            while True:
                file_name = input("Enter a file name: ").lower()
                file_path = os.path.join(current_directory, notes_directory, f"{file_name}.txt")
                if os.path.exists(file_path):
                    print("File already exists. Please choose a different name.")
                else:
                    break
            with open(file_path, 'w') as file:
                file.write('\n'.join(notes))
            print(f"File saved as {file_path}")
            break
        elif user_input != "exit":
            notes.append(user_input)
    print("Exiting...")