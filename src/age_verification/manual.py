import subprocess

age = input("Enter your age: ")

try:
    age = int(age)
except ValueError:
    print("Invalid option")
    print()
    subprocess.call(["python", "src/age_verification/manual.py"])

if age <= 18:
    print("You are a minor!")
    print(":)")
    print()
    subprocess.call(["python", "src/age_verification/end.py"])
if age >= 18:
    print("You are an adult!")
    print(":)")
    print()
    subprocess.call(["python", "src/age_verification/end.py"])