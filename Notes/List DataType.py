# Lists --> Ordered sequence of elements
#       --> written between [] separated by commas(,)
#       --> lists are mutable (changeable)


message = ["Yash", "is", "learning", "Python."]  # list of strings
numbers = [10, 20, 30, 40]  # list of numbers
print(len(message))  # gives the number of elements in the list


# Indexing works the same as in strings
# to access an element just --> list[index]
print(message[0])  # prints 'Yash' because that is on index 0 in message
print(numbers[2])  # prints 30


# index can have 2 upto 2 values
# list[start:stop] --> starts at given value stops at one less than given value
print(message[0:2])
print(numbers[0:3])
print(message[:4])
print(numbers[2:])


# changing lists
num = [10, 12, 21]
print(num)
num[1] = 7  # changes the element present on the given index to new provided element
print(num)


# list methods --> functions associated with lists
#                  1) list.index() --> gives the index of the given element
#                  2) list.append() --> adds the given element to the list
#                  3) list.insert(index, element) --> inserts an element at the given index
#                  4) list.remove(element) --> removes the given element
#                  5) list.pop --> removes the given index's element
#                  6) "" in list --> checks whether the given element is in the list or not
#                  7) list.sort() --> sorts the list, by default in Ascending order
#                                 --> True = Descending
#                                 --> False = Ascending order
#                  8) list.reverse() --> reverses the order of items of list
#                  9) list.clear() --> deletes every element of list
#                  10) list.copy() --> copies all the contents of the given list
#                  11) list.extend(other_list) --> appends all the elements of other_list at the end of the list

fruits = ["Apple", "Pineapple", "Mango", "grapes"]
print("Fruits = " + str(fruits))
print("Apple" in fruits)
print(fruits.index("Mango"))
print(fruits.append("guava"))
print(fruits.insert(0, "Watermelon"))
print(fruits.remove("Pineapple"))
print(fruits.pop(3))
print("fruits after list operations = " + str(fruits))

Z = [10, 4, 3, 54, 32, 22]
print("list before sorting " + str(Z))
Z.sort()
print("list after sorting " + str(Z))
Z.reverse()
print("Reversed list " + str(Z))
A = Z.copy()
print("A = Copied list from Z : " + str(A))
B = [0, 1, 2]
Z.extend(B)
print("Extended list Z : " + str(Z))
Z.clear()
print("Cleared list : " + str(Z))


# iterating over lists
animals = ["Lion", "Tiger", "Dolphin", "Monkey"]
characters = 0
for animal in animals:
    characters += len(animals)
print("Total characters in list : {}".format(characters))
print("Average length of each element : {}".format(characters / len(animals)))


# enumerating lists
winners = ["Yash", "Utkarsh", "Rahul", "Raj"]
for index, person in enumerate(winners):
    print("{} - {}".format(index+1, person))


# list comprehensions --> creating lists faster
#                     --> multiple = [x*7 in range (1,11)]    # will create a list of multiples of 7
#                                                             # this is a list comprehension
#
#                     --> to do so without comprehensions you have to  either manually type the list
#                         or do something like this :
#                               --> multiple = []
#                                   for x in range(1,11):
#                                      multiple.append(x * 7)
#                                   print(multiple)

