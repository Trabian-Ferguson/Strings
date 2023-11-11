# Program Name: Lab9.py 
# Course: IT1114/Section 01
# Student Name: Trabian Ferguson
# Assignment Number: Lab9.py
# Due Date: 11/5/2023
# Purpose: This program will verify a password that has the required characters.


pw = input("Password:")

length = False
conUpper = False
conLower = False
conSpec = False
conNum = False

if len(pw) >= 9:
    length = True


for char in pw:
    if char.isupper():  
        conUpper = True
    if char.islower():
        conLower = True
    if char in "#!$_":
        conSpec = True
    if char.isnumeric():
        conNum = True

if length and conUpper and conLower and conSpec and conNum:
    print("Valid Password")
else:
    print("Invalid Password")


        





# password must be 9 characters (in )
# password must include a upper and lower letter (in)
# password must include one number (out)
# password must inlcude one of the following special charcters: #,!,$,_ (out)


