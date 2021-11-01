import random
import string
import os

chars = string.printable
website = [""]
password = [""]

def createPass():
    global website
    global password

    while True:
        website = input("What is the name of the web app?: ")
        password_len = int(input("How many characters do you want in your password?: "))
        password = ""
        for x in range(0,password_len):
            password_char = random.choice(chars)
            password = password + password_char
        
        answer = input("Do you want to add more passwords? :")
        answer = answer.lower()
        if(answer == "yes"):
            continue
        else:
            break

def output():
    print("Your creditantials are as follows: ")
    print("----------------------------------")
    print("Website:",website)
    print("Password:",password)

def checkFileExist():
    if os.path.exists("passwords.txt"):
        pass
    else:
        file = open("passwords.txt","w")
        file.close

def appendNew(website,password):
    with open("passwords.txt","a") as file:
        file.write("Website: " + website)
        file.write(" Password: " + password + "\n")

createPass()
checkFileExist()
appendNew(website,password)
output()
