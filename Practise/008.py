# check whether the given number is even or odd and print the appropriate message
# in the form "the given number x is y" where x is the number and y is odd/even.

num = int(input("Enter the number:"))
if num % 2 == 0:
    print("The number {} is {}".format(num, "even"))
else:
    print("The number {} is {}".format(num, "odd"))

