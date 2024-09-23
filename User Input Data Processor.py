# Task 1: Input Length Validator
# Write a script that asks for and checks the length of the user's first name and last name.
# Both should be at least 2 characters long. If not, print an error message.

# step 3: add a min length of 2 characters. Add a line of code that prints out an error message for not meeting the min length. 
min_length = 2

# step 1: ask for user input
first_name = input("Tell us your first name: ")
last_name = input("Tell us your last name: ")
full_name = first_name + " " + last_name

# step 2: check the length of the first and last name
if (min_length <= len(first_name)) and isinstance(first_name, str) and first_name.isalpha():
    if len(last_name) >= 2 and isinstance(last_name, str) and last_name.isalpha():
        print(f"You full name is {full_name}.")
else:
    print("ERROR: you have not met the required min length or you have not included only alphabetical values in your inputs")

