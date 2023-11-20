import subprocess
import datetime

year = input("Enter your Birth Year: ")

try:
    year = int(year)
except ValueError:
    print("Invalid option")
    print()
    subprocess.call(["python", "src/age_verification/year.py"])

# Gets the current year
current_year = datetime.datetime.now().year

age = current_year - int(year)

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