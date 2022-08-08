# def hello(parameters):    // use 'def' to define a function, 'hello' here is the name of
#     -body-                   the function, use () to set up parameters for the function.
#     -body-
#
# hello(parameters)         // calling the function

def greeting(name):
    print("Welcome " + name)


greeting("Yash")  # will print - Welcome Yash


# Why need functions??
#     to simply avoid code duplication and make your code look clean and easily readable/understandable
#     ex - in this above function if you want to print " welcome 'name' " for 10 people
#          you can simply use 'greeting(name)' 10 times instead of writing
#          print("welcome" + "name") 10 times
#          in this particular example writing 'print()' 10 times doesn't seem much work
#          but, what about when you want to input two numbers and then add them for 10
#          or maybe 100 times or solving more complex problems --> functions come in handy!!

def add1(num1, num2):
    summ = num1 + num2
    print(summ)


add1(10, 20)  # just call the function and give parameters as many times as you want two numbers added
add1(177, 23)


# another way of finding sum using function
def add2():
    num1 = int(input("Enter number1 : "))
    num2 = int(input("Enter number2 : "))
    sum = num1 + num2
    print("The sum is : " + str(sum))


add2()
add2()  # just call the function as many times as you want sum of two numbers


# use input function to get user-defined inputs
#   syntax --> datatype(input("input message"))
#              ex - int(input(""))  --> inputs integer value
#                 - float(input())  --> inputs decimal(float) value


# returning values --> use 'return' function
#                      now as you are returning/taking some value out of the function, simply
#                      calling it would not work - you have to store this value in a variable
#                      and then print it

def triangle(base, height):
    return base * height / 2


area = triangle(10, 5)
print("The are of triangle is : " + str(area))


# recursion --> The process of defining a problem (or the solution to a problem)
#               in terms of (a simpler version of) itself.

def countdown(n):
    while n >= 0:
        print(n)
        n -= 1


countdown(2)  # output --> 2
#                          1
#                          0


def count(n):             # defining the same function recursively
    print(n)
    if n > 0:
        countdown(n - 1)  # recursive call


count(2)                  # displays the same output as the above countdown() function,
                          # just this time the code is simpler

