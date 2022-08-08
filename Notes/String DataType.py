# Strings  --> used to represent a piece of text
#          --> written between ""

name = "Yash"  # Declaring a string

greet = "Hello" + "Yash"  # Adding two strings
print(greet)

a = "hello" * 2  # Multiplying a string with an integer
print(a)

# String Indexing --> "YASH" - Y = 0th index
#                            - A = 1st index
#                            - S = 2nd index
#                            - H = 3rd index
#
# negative indexing -->      - Y = -4th index
#                            - A = -3rd index
#                            - S = -2nd index
#                            - H = -1th index
Name = "Yash"
letter1 = Name[0]
let1 = Name[-4]
print(letter1)  # prints Y, because that is the on 0 index
print(let1)  # prints Y, because that is the on -4 index

# string slicing --> cutting out portion of a string
# [start:stop] --> where to start slicing and where to stop
#                  (stops at one less than given value)
#                  if nothing provided in one place it takes the default as
#                  start or end of string depending on the place it is placed.
name = "Yash"
index = name[0:2]
index2 = name[:2]
print(index + " " + index2)  # prints the same for both i.e. --> Ya

fruit = "pineapple"
ind = fruit[:4]
ind2 = fruit[4:]
print(ind)  # prints --> pine
print(ind2)  # prints --> apple

# creating new strings --> strings are immutable(cannot be modified)
#                          so, if you do something like --> greet = "Tello"
#                                                           greet[0] = "H"    # trying to replace
#                                                           print(greet)        'T' with 'H'
#
#                          it will show error, because this simply is not allowed
#                          instead use something like
greet = "Tello"
new = greet[0:0] + "H" + greet[1:]  # greet[0:0] --> starting from 0 whatever is on 0 replace with 'H'
#                then add the rest of string to it
print(new)  # will print "Hello"

# question: make pineppple --> pineapple
fru = "pineppple"
print("Original String: " + fru)
fruit = fru[0:4] + "a" + fru[5:]
print("Changed string: " + fruit)


# String methods --> a function associated with a specific class(class here is string)
#                    1) string.index("") --> gives the index of the character
#                    2) "" in string --> checking for substring
#                    3) string.upper() --> convert to UPPERCASE
#                    4) string.lower() --> convert to lowercase
#                    5) string.strip() --> deletes the surrounding blank spaces
#                                      --> lstrip() : deletes everything left of string
#                                      --> rstrip() : deletes everything right of string
#
#                    6) string.isnumeric() --> checks whether string is made up of only numbers or not
#                    7) string.isalpha() --> checks whether the string is made up of only alphabets or not
#                    8) string.join() --> adding two or more strings
#                    9) string.split() --> splitting the string into individual words
#                    10) string.endswith --> to check whether a string ends with a particular word on  not

NewStr = "Hello, my name is Yash"
x = "."
print(NewStr.index("n"))
print("Y" in NewStr)
print(NewStr.upper())
print(NewStr.lower())

print(NewStr.strip())
print(NewStr.lstrip())
print(NewStr.rstrip())

print(NewStr.isalpha())
print(NewStr.isnumeric())

print(x.join(NewStr))  # will put a '.' after every character

print(NewStr.split())
print(NewStr.endswith("is"))

# Formatting strings --> use .format method
#                 {} --> placeholders, to show where the variables should be written
#                        then we pass the variables as a parameter to the .format method
naam = "Yash"
age = 18
formatting = "Hello {}, your age is {}".format(naam, age)
print(formatting)

price = 10.500
with_tax = price * 1.09
print("Base price: {: .2f}".format(price))  # .2f prints the value upto 2 decimal places ()
print("Taxed price: {: .2f}".format(with_tax))

num = 10.67546
print("Number {:>10.2f}".format(num))  # {:>10.2f} --> 10 spaces and 2 decimal places

# similarly, {:>4.5f} --> 4 spaces and 5 decimal places
#            {:>6.1f} --> 6 spaces and 1 decimal place
#             etc.etc.

