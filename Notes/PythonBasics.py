
# PyCharm Editor Shortcuts

#   cmd + / --> Comment
#   cmd + D --> Duplicate a piece of code
#   cmd + shift + up/down arrows --> To move  a line of code up or down
#   cmd + (-) --> To collapse a codeblock
#   cmd + (=) --> To expand a codeblock
#   cmd + Option + T --> Surround selected code with some template

#   control + G --> To select a particular word
#   control + G (again) --> To select similar next word
#   control + shift +G --> Deselect last selected word
#   cmd + control + G --> To select all similar words

#   control + shift + R --> To run the program
#   Shift + esc --> To exit run window


# Printing something onto the display.

print("Hello World")   # for words(Strings) use "" inside the ()
print(10)              # numbers don't require anything


# operators in python

#    * --> multiply
#    ** --> Power
#    + ---> Add
#    - --> Subtract
#    / --> normal division
#    % --> gives remainder of division

print(2 * 10)
print(2 ** 10)
print("Hello "*3)

print(10 + 4)
print("Hello" + " Yash")

print(10 - 5)

print(10 / 2)
print(13 / 2)
print(10 % 2)
print(13 % 2)

print(((2050 / 5) - 32) / 9)

# Assignment --> process of storing a value inside a variable
#   Variable --> names given to certain values in a program
#   Expression --> Combination of numbers, symbols or other variables that
#                  produce a result when evaluated.

name = "Yash"  # 'name' is the variable
number = 10

# Program to calculate Area of a rectangle
length = 10
width = 2
Area = length * width  # expression
print(Area)

# Program to calculate Area of a triangle
base = 6
height = 3
Area_of_Triangle = (base*height)/2
print("The area of triangle is : " + str(Area_of_Triangle))  # here we use str function
#                                                              because you cannot add a
#                                                              string to a number. 'str'
#                                                              explicitly converts the
#                                                              number to a string so
#                                                              that it can be added.
