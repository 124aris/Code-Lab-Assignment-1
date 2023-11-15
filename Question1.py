# Question 1:
# Function find_even_odd():
# Write a Python function called find_even_odd that takes a list of integers as input and 
# returns two separate lists—one containing the even numbers and the other containing the odd numbers.

def find_even_odd(numbers):
    numbers = [int(num) for num in numbers.split()];
    even_numbers = [];
    odd_numbers = [];
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num);
        else:
            odd_numbers.append(num);
    return even_numbers, odd_numbers;

numbers = input("Enter a List of Integers Separated by Spaces: ");
even_numbers, odd_numbers = find_even_odd(numbers);

print("Even numbers:", even_numbers);
print("Odd numbers:", odd_numbers);