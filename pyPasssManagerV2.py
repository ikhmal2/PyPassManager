import random
import string

chars = string.printable

while True:
    website = input("What is the name of the web app?: ")
    password_len = int(input("How many characters do you want in your password?: "))
    password = ""
    for x in range(0,password_len):
        password_char = random.choice(chars)
        password = password + password_char
    break

print("Your creditantials are as follows: ")
print("----------------------------------")
print("Website:",website)
print("Password:",password)

