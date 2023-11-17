# Question 4:
# Custom Question:
# Create a file with appropriate file name, which contains only a collection of functions.
# In this file, write a set of functions to create your very own library.
# After creating this library, create another program file and
# write a program which makes use of most/all of the functions you have created in your custom library.
# The sky’s the limit.

def sum(first_number, second_number):
    return first_number + second_number;

def subtract(first_number, second_number):
    return first_number - second_number;

def multiply(first_number, second_number):
    return first_number * second_number;

def divide(first_number, second_number):
    if second_number == 0:
        return "Cannot divide by zero";
    return first_number / second_number;

def display_menu():
    print("Select operation:");
    print("1. Add");
    print("2. Subtract");
    print("3. Multiply");
    print("4. Divide");
    print("5. Exit");