import os

def dollpycode():
    runpyide = []
    print("Welcome to DollPyCode! (type 'exit' to exit or 'run' to run or 'save' to save)")
    pyideyou = ""
    
    current_directory = os.path.dirname(os.path.abspath(__file__))
    subdirectory = "saves\\pycodes"
    
    # Verifique se o subdiretório existe e crie se necessário
    if not os.path.exists(os.path.join(current_directory, subdirectory)):
        os.makedirs(os.path.join(current_directory, subdirectory))
    print("----------")
    while pyideyou != "exit":
        print("")
        pyideyou = input("")
        if pyideyou == "run":
            print(f"Code:\n{runpyide}")
            print("")
            exec('\n'.join(runpyide))
            runpyide.clear()
        elif pyideyou == "save":
            while True:
                name = input("Type a name: ").lower()
                file_path = os.path.join(current_directory, subdirectory, f"{name}.py")
                if os.path.exists(file_path):
                    print("File already exists. Please choose a different name.")
                else:
                    break
            with open(file_path, 'w') as file:
                file.write('\n'.join(runpyide))
            print(f"File saved as {file_path}")
            break
        else:
            runpyide.append(pyideyou)
    print("Exiting...")