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
print("PASSWORD GENERATOR"
      "\n------------------")
print()
print("This password generator will create a password between "
      "10 and 20 characters in length, using digits (0 to 9), "
      "letters (A to z), and special characters (%, $, etc.).")
print()

# Ask for user input
print("Please enter the MINIMUM number of the following that you need "
      "in your password. NOTE: Minimum values must be numbers greater "
      "than or equal to 0.")
print()

okay = False
while not okay:
    done = False
    while not done:
        try:
            numOfLetters=int(input("* Minimum number of letters: "))
            while numOfLetters < 0:
                print("ERROR: You entered a number less than 0. Please try again.")
                numOfLetters=int(input("* Minimum number of letters: "))
            done=True
        except ValueError:
            print("ERROR: You did not enter a number. Please try again.")
    print()
    done=False
    while not done:
        try:
            numOfDigits=int(input("* Minimum number of digits: "))
            while numOfDigits < 0:
                print("ERROR: You entered a number less than 0. Please try again.")
                numOfDigits=int(input("* Minimum number of digits: "))
            done=True
        except ValueError:
            print("ERROR: You did not enter a number. Please try again")
    print()
    done=False
    while not done:
        try:
            numOfSpecial=int(input("* Minimum number of special characters: "))
            while numOfSpecial < 0:
                print("ERROR: You entered a number less than 0. Please try again.")
                numOfSpecial=int(input("* Minimum number of special characters: "))
            done=True
        except ValueError:
            print("ERROR: You did not enter a number. Please try again")
    print()
    if (numOfLetters+numOfDigits+numOfSpecial > 20):
        print("ERROR: The sum of the minimum number of letters, digits, and special characters "
              "must be less than or equal to 20. Please try again.")
    else:
        okay=True
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







        





