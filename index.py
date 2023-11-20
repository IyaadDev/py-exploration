# py exploration - @IyaadDev

import subprocess

print("Welcome to my projects!")
print()
print("Select a menu option to begin:")

options = {
    "1": {
        "name": "Age Verification",
        "path": "projects/age_verification.py",
        "description": "A simple age verification program."
    },
    "2": {
        "name": "Divisible by 3",
        "path": "projects/divisible_by_3.py",
        "description": "A program that checks if a number is divisible by 3."
    },
    "3": {
        "name": "Even or Odd",
        "path": "projects/even_or_odd.py",
        "description": "A program that checks if a number is even or odd."
    },
    "4": {
        "name": "Fibonacci Sequence",
        "path": "projects/fibonacci_sequence.py",
        "description": "A program that prints the Fibonacci sequence."
    }
}

for key, value in options.items():
    print(f"{key}. {value['name']} - {value['description']}")

selected_option = input("Enter a number: ")

if selected_option in options:
    subprocess.call(["python", options[selected_option]["path"]])