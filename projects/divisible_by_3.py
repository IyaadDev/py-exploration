# Divisible by 3
# # py exploration - @IyaadDev

import subprocess

print("Divisible by 3 is now running...")

print()

number = int(input("Enter a number: "))
if number % 3 == 0:
    print(f"{number} is divisible by 3.")
else:
    print(f"{number} is not divisible by 3.")

subprocess.call(["python", "system\completion.py"])