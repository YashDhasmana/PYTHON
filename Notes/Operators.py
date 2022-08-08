# Comparison Operators
#     > --> greater than
#     < --> less than
#     >= --> greater than equal to
#     <= --> less than equal to
#     == --> equality operator
#     != --> not equal to

print(10 > 1)      # True
print(5 < 4)       # False
print(10 >= 10)    # True
print(10 <= 12)    # True
print(10 == 10)    # True
print(10 != 5)     # True


print("cat" == "dog")    # False
print("cat" == "cat")    # True
print(1 == 1)            # True
print(1 == '1')          # False - because 1 is int and '1' is string


# Logical Operators
#   and operator - both expressions need to be true at the same time.
#   or operator - expression will be True if one is True and False if both are False
#   not operator - inverts the value of what is in front of it

print(1 == 1 and "cat" == "cat")                               # True
print(1 == 1 and "dog" == "cat")                               # False
print("yellow" > "cyan")  # here alphabetical order is taken   # True
print("cyan" > "yellow")                                       # False
print("yellow" > "cyan" and "brown" > "magenta")               # False


print("yellow" > "cyan" or "brown" > "magenta")                # True
print(1 == 1 or 20 != 1)                                       # True


print(not 41 == "Answer")                                      # True
print(not "Hello" == "Goodbye")                                # True

