# This code intakes user input to augment a user inputted password by a 
# user inputted integer. The password is outputted without any spaces 
# and all uppercase. 

aug = int(input("Enter rotation length of characters: "))
password = input("Enter the password to encode: ")

password = password.replace(" ", "")
password = password.upper()
l = list(password)

for x in l:
    q = 65 + (((ord(x) + aug) % 65) % 26)
    print(chr(q), end ='')
