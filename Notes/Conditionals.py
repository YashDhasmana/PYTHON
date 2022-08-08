# if statements
# syntax --> if (parameters):
#              -body-

name = "Yash"
if (len(name)) > 4:              # len() function --> gives the length of the string
    print("Valid Username")

# else statements
#  syntax --> else:
#               -body-

name = "Yash"
length = len(name)

if length > 4:
    print("Valid Username")
else:
    print("Invalid Username")

# nested if-else
# syntax --> if(parameters):
#               -body-
#            elif(parameters):     # can add as many elif statements as required
#               -body-
#            else:
#               -body-

number = 10
if number < 0:
    print("Negative Number")
elif number > 0:
    print("Positive Number")
else:
    print("Number is Zero")

