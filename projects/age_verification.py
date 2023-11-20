import subprocess
print("Welcome to the age verification spot!")
print()

print("Select a way to verify your age:")
options = {
    "1": "Birth Year",
    "2": "Age"
}

for key, value in options.items():
    print(f"{key}. {value}")

selection = input("Enter a number: ")

if selection == "1":
    subprocess.run(["python", "src/age_verification/year.py"])
elif selection == "2":
    subprocess.run(["python", "src/age_verification/manual.py"])
else:
    print("Invalid selection. Please try again.")
