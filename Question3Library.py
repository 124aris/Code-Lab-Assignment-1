# Question 3: 
# You are required to create a Python library that provides various string manipulation functions.
# Your library should include the following functionalities:
# 1.Reverse String:
# Implement a function reverse_string(s) that takes a string s as input and returns the reversed string.
# 2.Count Vowels:
# Create a function count_vowels(s) that takes a string s as input and
# returns the count of vowels (both uppercase and lowercase) in the string.
# 3.Title Case:
# Implement a function title_case(s) that takes a string s as input and
# returns the string with the first letter of each word capitalized.
# Substring Search:
# 4.Remove Whitespace:
# Implement a function remove_whitespace(s) that takes a string s as input and
# returns the string with all whitespace characters removed.
# Task:
# Share your Python script containing the library functions. Include a document with the usage examples and test cases.

# 1.Reverse String:
def reverse_string(string):
    return string[::-1];

# 2.Count Vowels:
def count_vowels(string):
    count = 0;
    vowels = "aeiouAEIOU";
    for char in string:
        if char in vowels:
            count += 1;
    return count;

# 3.Title Case:
def title_case(string):
    return string.title();

# 4.Remove Whitespace:
def remove_whitespace(string):
    return ''.join(string.split());