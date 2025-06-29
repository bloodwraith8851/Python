# single line comment

# this is a single line comments

# multi-line comment

# this is a multi-line comment
# we can use triple quotes for multi-line comments

""" we can use triple quotes for multi-line comments 
    this is a multi-line comment
we can use triple quotes for multi-line comments """

# u can comment multiple lines using #  using  ctrl + / in most code editors

# doc string

# docstring is a special type of comment used to describe the purpose of a function, class, or module.
# docstring is written inside triple quotes
def add(a, b): # declare a function with two parameters a and b
    """This function adds two numbers.""" # docstring for the function
    return a + b # docstring for the function

# def example():
name_input = input("Please enter your name: ")  # take input from the user   1 step
age_input = int(input("Please enter your age: "))  # take input from the user 2 step
def greet_user():  # 4step
    """ This function takes a person's full name and age as input and return a greeting message."""
    message = f"Hello {name_input}! you are {age_input} years old. Glad to meet You!"
    print (message)  # print the message

greet_user()  # call the function to greet the user 3 step
