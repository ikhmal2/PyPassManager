import random
import string
import os

chars = string.printable
website = []
password = []

def createPass():
    global website
    global password

    while True:
        website.append(input("What is the name of the web app?: "))
        password_len = int(input("How many characters do you want in your password?: "))
        create_password = ""

        for x in range(0,password_len):
            password_char = random.choice(chars)
            create_password = (create_password + password_char)
         
        password.append(create_password)
        
        answer = input("Do you want to add more passwords? :")
        answer = answer.lower()
        if(answer == "yes"):
            continue
        else:
            break

def output():
    print("Your creditantials are as follows: ")
    print("----------------------------------")

    for w in website:
        for p in password:
            print("Website:",w)
            print("Password:",p)

def checkFileExist():
    if os.path.exists("passwords.txt"):
        pass
    else:
        file = open("passwords.txt","w")
        file.close

def appendNew(website,password):

    for w in website:
        for p in password: 
            with open("passwords.txt","a") as file:
                file.write("Website: " + w)
                file.write(" Password: " + p + "\n")

createPass()
checkFileExist()
appendNew(website,password)
output()