# Tuples --> Very similar to lists
#        --> sequence of elements of any type and are immutable
#        --> tuples are created inside ()

name = ('Yash', 'Dhasmana')  # a tuple of strings
nums = (12, 43, -23, 0)  # a tuple of numbers

# splitting tuples --> unpacking
#                  --> for n elements in a tuple to n different elements

print("name :" + str(name))
first, second = name
print("First name: " + first)
print("Surname: " + second)

print("Numbers:" + str(nums))
even, odd, negative, zero = nums
print("Even number:" + str(even))
print("Odd number: " + str(odd))
print("Negative number:" + str(negative))
print("Zero:" + str(zero))

# Tuple Methods
#   1) tuple.count() --> counts the number of occurrences of the given element in the tuple
#   2) tuple.index() --> gives the index of the element provided
#                    --> Takes upto 3 arguments - (element, start, end)

fruits = ('Mango', 'Apple', 'Grapes', 'Apple', 'Pineapple', 'Guava')
c = fruits.count('Mango')
print("Index of element 'Mango' in the tuple is: " + str(c))
i = fruits.index('Grapes')
print("Index of element 'Grapes' in the tuple is: " + str(i))

numbers = (1, 2, 3, 2, 5, 6, 2, 3, 4, 5, 1, 1, 0)
index = numbers.index(1, 8)                       # (element, start) --> find the index of given element
print(index)                                      #                      starting from the start index onwards

index2 = numbers.index(2, 2, 5)                   # find the index of the given element between the start and end
print(index2)                                     # indexes

