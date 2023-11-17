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

import Question3Library;

string = input("Enter a String of your Choice: ");
reversed_string = Question3Library.reverse_string(string);
print("Reversed String:", reversed_string);
vowel_count = Question3Library.count_vowels(string);
print("Vowel Count:", vowel_count);
title_cased = Question3Library.title_case(string);
print("Title Cased String:", title_cased);
without_whitespace = Question3Library.remove_whitespace(string);
print("String without Whitespace:", without_whitespace);