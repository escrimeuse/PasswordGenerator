"""
Password Generator
Made by: Cathryn Griffiths
         cathryn.griffiths@gmail.com
         http://cathryn.dersam.net
"""

# Modules
import random
import string


# Welcome message
print("PASSWORD GENERATOR")
print("------------------")
print()
print("This password generator will create a password between")
print("10 and 20 characters in length, using digits (0 to 9),")
print("letters (A to z), and special characters (%, $, etc.).")
print()

print("Enter the MINIMUM number of the following that you need")
print("in your password.")
print("NOTE: Minimum numbers must be greater than or equal to 0.")
print()
numOfLetters=int(input("\tLetters: "))
while numOfLetters < 0:
    print()
    print("ERROR: \tThe minimum number of letters must be greater")
    print("\tthan or equal to 0.")
    print()
    numOfLetters=int(input("\tPlease enter the minimum number of letters: "))
print()
numOfDigits=int(input("\tDigits: "))
while numOfDigits < 0:
    print()
    print("ERROR: \tThe minimum number of digits must be greater")
    print("\tthan or equal to 0.")
    print()
    numOfDigits=int(input("\tPlease enter the minimum number of digits: "))
print()
numOfSpecial=int(input("\tSpecial characters (ex: $, %, &): "))
while numOfSpecial < 0:
    print()
    print("ERROR: \tThe minimum number of special characters must")
    print("be greater than or equal to 0.")
    print()
    numOfSpecial=int(input("\tPlease enter the minimum number of special characters: "))
    
print()


# Create password
passwordList=[]

for x in range(numOfDigits): # insert numbers into list
    passwordList.append(random.choice(string.digits))

for x in range(numOfLetters): # insert letters into list
    passwordList.append(random.choice(string.ascii_letters))
        
for x in range(numOfSpecial): # insert special characters into list
    passwordList.append(random.choice(string.punctuation))

chooseFrom=string.digits+string.ascii_letters+string.punctuation
minCharacters=numOfDigits+numOfLetters+numOfSpecial # the total minimum number of characters
if minCharacters >=10:
    moreCharacters=random.randint(0,20-minCharacters) # additional number of characters
else:
    moreCharacters=random.randint(10-minCharacters,20) # additional number of characters to bring password length between 10 and 20

for x in range(moreCharacters): # insert additional characters into list
    passwordList.append(random.choice(chooseFrom))


random.shuffle(passwordList) # shuffle the password list
password=""
for x in range(0,len(passwordList),1): # create password string
    password=password+passwordList[x]

# Display password
print("Your password is:",password)

# Exit message
print()
print("All done. Goodbye!")







        





