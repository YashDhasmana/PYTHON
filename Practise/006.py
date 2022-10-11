# WAP to count positive and negative numbers in a list


ls = [1, -3, 4, 12, - 9, 5, 11]
positive = 0
negative = 0
for num in ls:
    if num > 0:
        positive += 1
    else:
        negative += 1
print("Positive Numbers: ", positive)
print("Negative Numbers: ", negative)
