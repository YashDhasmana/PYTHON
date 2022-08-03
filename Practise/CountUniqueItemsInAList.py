# WAP to count unique items in a list

ls = [10, 2, 3, 4, 2, 3, 12, 32, 43, 23, 23, 21, 10]
lis = []
count = 0
for ele in ls:
    if ele not in lis:
        count += 1
        lis.append(ele)

print("The unique items in the list are:" + str(lis))
