# dictionaries --> the values in dictionaries takes the form of a key:value pair
#              --> use {} to define  a dictionary
#              --> dictionary = {Key:Value}
#              --> both keys and values can be of the same datatype
#              --> key is used to access its associated value
#              --> they are mutable

file_counts = {"jpg": 10, "txt": 12, "py": 20}  # a dictionary
print(file_counts)

# Accessing a value using its key
print(file_counts["txt"])  # should print 12 because that is the

# value associated with the key "txt"
# some dictionary methods

print("jpg" in file_counts)
print("csv" in file_counts)

print("Original dict: " + str(file_counts))
file_counts["csv"] = 14  # adding a new pair to the dictionary
print("After adding an element: " + str(file_counts))

del file_counts["csv"]  # deleting a pair from dictionary
print("After deletion: " + str(file_counts))

# iterating in a dictionary
products = {"Laptops": 10, "Phones": 20, "TV": 12}
for extension in products:
    print(extension)  # outputs the keys of the dictionary

file_counts = {"jpg": 10, "txt": 12, "py": 20}
for ext, amount in file_counts.items():
    print("There are {} files with .{} extension".format(amount, ext))

keys = products.keys()  # prints the keys of the dictionary
print(keys)
values = products.values()  # prints the values of the dictionary
print(values)


# counting the number of occurrences of the letters in a word
def count_letters(text):
    result = {}
    for letter in text:
        if letter not in result:
            result[letter] = 0
        result[letter] += 1
    return result


occu = count_letters("abcdytrytaabc")
print(occu)
