# Activity X.X.X: An introduction to Python.
# File: HW8_talmeida.py
# Date: 25 October 2018
# By: Tessca Almeida
# talmeida
# Section: 2
# Team: 40
#
# ELECTRONIC SIGNATURE
# Tessca Almeida
#
# The electronic signature above indicates that the program
# submitted for evaluation is my individual work. I have
# a general understanding of all aspects of its development
# and execution.
#
# This code intakes user input to augment a user inputted password by a 
# user inputted integer. The password is outputted without any spaces 
# and all uppercase. 

#---------------------------------------------------
#  Inputs
#---------------------------------------------------
aug = int(input("Enter rotation length of characters: "))
password = input("Enter the password to encode: ")
#---------------------------------------------------
#  Computations
#---------------------------------------------------
password = password.replace(" ", "")
password = password.upper()
l = list(password)

for x in l:
    q = 65 + (((ord(x) + aug) % 65) % 26)
    print(chr(q), end ='')