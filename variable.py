# Variable: Variables are containers for storing data values.
"""
They are created when you assign a value to it
Variables do not need to be declared with any particular type, 
and can even change type after they have been set.
"""

x = 5
y = 2

# Casting: If you want to specify the data type of a variable, this can be done with casting.
print("# Casting: If you want to specify the data type of a variable, this can be done with casting.")
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

# Get the Type: You can get the data type of a variable with the type() function.
print("# Get the Type: You can get the data type of a variable with the type() function.")
print(type(x))
print(type(y))

# Single or Double Quotes?: String variables can be declared either by using single or double quotes:
print("# Single or Double Quotes")
x = "Vinay"
# is the same as
x = 'Vinay'
print(x)

# Case-Sensitive: Variable names are case-sensitive.
# This will create two variables:
print("# Case-Sensitive: Variable names are case-sensitive. This will create two variables:")
a = 4
A = "Sally"
# A will not overwrite a
print(A)
print(a)

# Rules for Python variables:
"""
1. A variable name must start with a letter or the underscore character
2. A variable name cannot start with a number
3. A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
4. Variable names are case-sensitive (age, Age and AGE are three different variables)
"""

# Legal variable names:
myvar = "Vinay"
my_var = "Vinay"
_my_var = "Vinay"
myVar = "Vinay"
MYVAR = "Vinay"
myvar2 = "Vinay"

# NOTE: Remember that variable names are case-sensitive

# Multi Words Variable Names: Variable names with more than one word can be difficult to read.
# There are several techniques you can use to make them more readable:

# Camel Case: Each word, except the first, starts with a capital letter:
myVariableName = "Vinay"

# Pascal Case: Each word starts with a capital letter:
MyVariableName = "Vinay"

# Snake Case: Each word is separated by an underscore character:
my_variable_name = "Vinay"

# Assign Multiple Values: Python allows you to assign values to multiple variables in one line:
print("# Assign Multiple Values")
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
# Note: Make sure the number of variables matches the number of values, or else you will get an error.

# One Value to Multiple Variables: And you can assign the same value to multiple variables in one line:
print("# One Value to Multiple Variables")
x = y = z = "Orange"
print(x)
print(y)
print(z)

# Unpack a Collection: If you have a collection of values in a list, tuple etc. Python allows you extract the values into variables. This is called unpacking.
print("# Unpack a Collection")
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# Output Variables: The Python print statement is often used to output variables. To combine both text and a variable, Python uses the + character:
print("# Output Variables")
x = "awesome"
print("Python is " + x)

# Global Variables: Variables that are created outside of a function (as in all of the examples above) are known as global variables.
print("Create a variable outside of a function, and use it inside the function")
x = "awesome"


def myfunc():
    print("Python is " + x)


myfunc()

"""
If you create a variable with the same name inside a function, 
this variable will be local, and can only be used inside the function. 
The global variable with the same name will remain as it was, global and with the original value.
"""
print("Create a variable inside a function, with the same name as the global variable")
x = "awesome"


def myfunc():
    x = "fantastic"
    print("Python is " + x)


myfunc()

print("Python is " + x)

# The global Keyword: Normally, when you create a variable inside a function,
# that variable is local, and can only be used inside that function.
# To create a global variable inside a function, you can use the global keyword.

print("If you use the global keyword, the variable belongs to the global scope:")


def myfunc():
    global x
    x = "fantastic"


myfunc()

print("Python is " + x)
