import random

# a function to shuffle all the characters of a string 
def shuffle(string):
  temp = list(string)
  random.shuffle(temp)
  return ''.join(temp)


# values according to ASCII Chart
# chooses one random char from given range in each line
upperCase_1 = chr(random.randint(65,90))
upperCase_2 = chr(random.randint(65,90))
upperCase_3 = chr(random.randint(65,90))
upperCase_4 = chr(random.randint(65,90))

lowerCase_1 = chr(random.randint(97,122))
lowerCase_2 = chr(random.randint(97,122))
lowerCase_3 = chr(random.randint(97,122))
lowerCase_4 = chr(random.randint(97,122))

specialChars_1 = chr(random.randint(33,38))
specialChars_2 = chr(random.randint(33,38))
specialChars_3 = chr(random.randint(63,64))

numbers_1 = chr(random.randint(48,57))
numbers_2 = chr(random.randint(48,57))
numbers_3 = chr(random.randint(48,57))


# randomly writing sequences that can later be added to make a strong random password 
pass_1 = (upperCase_1 + lowerCase_3 + numbers_2 + upperCase_4 + specialChars_3)
pass_2 = (lowerCase_1 + numbers_3 + specialChars_2 + lowerCase_4 + upperCase_2)
pass_3 = (numbers_1 + specialChars_1 + upperCase_3 + lowerCase_2)

strongPass = (pass_1 + pass_3 + pass_2)
superStrongPass = shuffle(pass_1 + pass_2 + pass_3)


# prompting user with options for a password 
print("choose from the options below")
print("A - strong random password")
print("B - super strong random password")
choice = input("Enter your choice (A / B) : ")

if choice == "A":
    print("Here is your password : " + strongPass)
elif choice == "B":
    print("Here is your password : " + superStrongPass) 
else:
    print("Enter a valid option") 
