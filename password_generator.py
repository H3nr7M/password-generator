import random
import string

# define a function to generate a random password
def generate_password(length):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ""
    for i in range(length):
        password += random.choice(chars)
    return password

# prompt the user for the length of the password they want to generate
length = int(input("Enter length of password: "))

# generate the password and display it to the user
password = generate_password(length)
print(f"Your password is: {password}")
