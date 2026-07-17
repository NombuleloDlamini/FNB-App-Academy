## user input ##

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
bio = input("Enter your bio message: ").strip(" ")
bio = bio.replace("I am", "I'm")

username = (first_name[0]+last_name).lower()
full_name = (first_name+" "+last_name).title()


print(f"{full_name}\n{bio}\nbio length:{len(bio)}")
