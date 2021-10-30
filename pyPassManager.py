import os

def checkExistance():
    if os.path.exists("info.txt"):
        pass
    else:
        file = open("info.txt",'w')
        file.close

def appendNew():
    file = open("file.txt",'a')

    print()
    print()

    userName = input("Enter the user name: ")
    password = input("\nEnter password: ")
    website = input("Enter the website address: ")

    file.write("-----------------------------------")
    file.write(userName)
    file.write(password)
    file.write(website)
    file.write("----------------------------------")
    file.write("\n")
    file.close

def readPasswords():
    file = open("info.txt","r")
    content = file.read()
    file.close()
    print(content)

checkExistance()
appendNew()
readPasswords()
