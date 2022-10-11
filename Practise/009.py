# WAP to reverse a given number

num = int(input("Enter the number:"))
rev = 0
while num != 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num//10

print("Reversed number:" + str(rev))

