# Question 4:
# Custom Question:
# Create a file with appropriate file name, which contains only a collection of functions.
# In this file, write a set of functions to create your very own library.
# After creating this library, create another program file and
# write a program which makes use of most/all of the functions you have created in your custom library.
# The sky’s the limit.

import Question4Library;

while True:
    Question4Library.display_menu();
    choice = input("Enter Choice (1-5): ");
    if choice in ('1', '2', '3', '4'):
        first_number = float(input("Enter First Number: "));
        second_number = float(input("Enter Second Number: "));
        if choice == '1':
            print("Result:", Question4Library.sum(first_number, second_number));
        elif choice == '2':
            print("Result: ", Question4Library.subtract(first_number, second_number));
        elif choice == '3':
            print("Result: ", Question4Library.multiply(first_number, second_number));
        elif choice == '4':
            print("Result: ", Question4Library.divide(first_number, second_number));
    elif choice == '5':
        print("Exiting Calculator. Goodbye!");
        break;
    else:
        print("Invalid Input. Please Enter a Valid Option.");