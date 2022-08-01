# WAP to count Even and Odd numbers in a List

ls = [12, 3, 54, 1, 4, 6, 8, 13, 5]
even = 0
odd = 0
for num in ls:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1
print("Even: ", even)
print("odd: ", odd)
