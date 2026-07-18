"""1. Ask the user to input their secret password.
2. Use .strip() to clean up any accidental spaces they might have typed at the start or end.
3. Grab the very first letter and the very last letter of the password using string indexing.
4. Print a hint using an f-string that forces the letters into uppercase so they stand out. (e.g., “Your password hint: It starts with P and ends with N”).
"""

password = input("Enter your secret password: ").strip()
starts_with = password[0].upper()
ends_with = password[-1].upper()
print(f"Your password hint: It starts with {starts_with} and ends with {ends_with}")