# Write a Python program to count the number 4 in a given list using functions.

def list_count(nums):
    count = 0
    for num in nums:
        if num == 4:
            count = count + 1

    return count


print(list_count([1, 0, 6, 7, 8]))
print(list_count([1, 4, 6, 4, 7, 4]))
