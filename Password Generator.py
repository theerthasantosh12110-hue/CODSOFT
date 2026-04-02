import random

length=int(input("Enter the length of the password:"))

letters="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers="0123456789"
chars="!@#$%^&*"

all_chars=letters+numbers+chars

password=""

if length < 3:
    print("Password length should be at least 3!")
else:
    password += random.choice(letters)
    password += random.choice(numbers)
    password += random.choice(chars)

    for i in range(length-3):
        ch=random.choice(all_chars)
        password+=ch

    print("Generated password:", password)
input("Press Enter to exit...")