"""
Write a program to accept a valid password from user
Length of password should be 8-26 characters
At least 1 upper case letter, 1 lower case letter, 1 digit, 1 special character
Only @ # _ special characters allowed
"""
while True:
    password = input("Enter a password (enter exit to exit): ")
    valid = True
    message = []
    valid_characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890@#_"

    if password == "exit":
        exit()

    for char in password:
        if char not in valid_characters:
            message.append(char + " is not a valid character")

    if len(password)<8 and len(password)>26:
        message.append("Password is less than 8 characters or more than 26 characters")
        valid = False

    is_upper_present = False
    for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        if char in password:
            is_upper_present = True
            break

    if not is_upper_present:
        message.append("No upper case character found")
        valid = False

    is_lower_present = False
    for char in "abcdefghijklmnopqrstuvwxyz":
        if char in password:
            is_lower_present = True
            break

    if not is_lower_present:
        message.append("No lower case character found")
        valid = False


    is_special_character_present = False
    for char in "@#_":
        if char in password:
            is_special_character_present = True
            break

    if not is_special_character_present:
        message.append("No special character found")
        valid = False

    is_number_present = False
    for char in "1234567890":
        if char in password:
            is_number_present = True
            break

    if not is_number_present:
        message.append("No number found")
        valid = False

    if not valid:
        for reason in message:
            print(reason)
    else:
        print("Password is valid")