# Completion.py

import subprocess

print()
print("What would you like to do now?")

options = ["Yes", "No"]

# Enter Y or N, ignore casing

for option in options:
    print(option)

print("Enter Y or N")
selected_option = input("Enter an option: ")

if selected_option == "Y" or selected_option == "y":
    subprocess.call(["python", "../index.py"])
elif selected_option == "N" or selected_option == "n":
    print()
    print("Would you like to exit this program?")
    print("1 - Yes")
    print("2 - No")
    print("Enter 'Y' or 'N' to continue.")
    end_option = input("Enter an option: ")
    if end_option == "Y" or end_option == "y":
        print("Exiting...")
        exit()
    elif end_option == "N" or end_option == "n":
        subprocess.call(["python", "system/completion.py"])
    else:
        print("Invalid option. Exiting...")
        exit()
else:
    print("Invalid option. Exiting...")
    exit()