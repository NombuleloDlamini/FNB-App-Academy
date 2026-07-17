## Getting user input ##

first_name = input("Enter your first name: ")
surname = input("Enter your surname: ")
age = int(input("Enter your age: "))
favourite_number = float(input("What's your favourite number? "))


## Displaying ##
print(f"{"Welcome"}, {first_name} {surname}!")
print(f"{first_name.upper()}\n{first_name.title()}")
print(f"{"Age in months: "}{age*12}")
print(f"{"favourite number rounded to nearest 2: "}{round(favourite_number,2)}")
print(f"first_name:{type(first_name)}, surname:{type(surname)}, age:{type(age)}, favourite_number:{type(favourite_number)}")

