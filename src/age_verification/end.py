#end
import subprocess
print()
print("Would you like to restart the program?")
print("1. Yes")
print("2. No")
print()

restart = input("Enter a number: ")

if restart == "1":
    subprocess.call(["python", "projects/age_verification.py"])
if restart == "2":
    print("Goodbye!")
    subprocess.call(["python", "index.py"])