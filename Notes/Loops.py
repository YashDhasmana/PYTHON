# Loops - sequence of instructions that are repeated until a certain condition is met
# while loop
# syntax --> while(parameters):
#               -body-

num = 0
while num < 2:
    print("Number is less, num= " + str(num))
    num = num + 1  # add 1 to num and store it in num.
print("x = " + str(num))

# for loop --> iterates over a sequence of values
# syntax --> for x in range(parameters):
#               -body-

for x in range(5):  # range starts from 0 and ends at one less than the given value
    print(x)  # in this case it's 0 - 4

# the range function can have upto 3 parameters
# (start, stop)  --> start at the given value, ends at one less than given value
# (start, stop, step)

product = 1
for n in range(1, 6):
    product = product * n
print("1*2*3*4*5 = " + str(product))

for z in range(1, 11, 2):  # Print numbers between 1 and 10 with a gap of 2(basically - odd numbers)
    print(z)

# break statement  --> To break out of the loop. anything written below break will never
#                      get executed. can be used in 'for' as well as 'while' loops.
for num in range(3):
    print(num)  # will print --> 0, 1, 2.

for num in range(3):
    print(num)
    break  # will break out of the loop after printing the first value in the given range.

for num in range(100):
    if num == 3:
        break
    print(num)   # will print --> 0, 1, 2, end
print("end")


# continue statement --> To skip a particular part of the code
for i in range(5):
    i = i + 1
    if i == 1:
        continue
    print(i)    # will skip 1 in the output and print the rest because we used continue statement

