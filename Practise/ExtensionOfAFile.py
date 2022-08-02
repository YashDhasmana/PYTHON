# Write a Python program to accept a filename from the user and print the
# extension of that.

file = input("Enter the filename:")
exs = file.split(".")
ext = exs[-1]
print("The extension of the given file is: " + ext)
