# Test whether a passed letter is a vowel or not

letter = input("Enter the letter:")
if letter in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):
    print("The letter  '{}'  is a vowel".format(letter))
else:
    print("The letter  '{}'  is a consonant".format(letter))
