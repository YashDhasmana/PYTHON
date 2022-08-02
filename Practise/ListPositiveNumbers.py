# WAP to print positive numbers in a list


ls = [1, -3, 4, 12, - 9, 5, 11, -10]
for num in ls:
    if num > 0:  # same applies for negative numbers too just use (num < 0)
        print(num, end=" ")
