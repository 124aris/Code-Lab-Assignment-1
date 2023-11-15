# Question 2:
# Function analyze_list():
# Write a Python function named analyze_list that takes a list of numbers as input and
# returns a list containing the following information:
# 1.Length: The total number of elements in the list
# 2.Sum: The sum of all numbers in the list.
# 3.Average: The average (mean) of the numbers.

def analyze_list(numbers):
    numbers = [int(num) for num in numbers.split()];
    if not numbers:
        return "List is Empty";
    else:
        length = len(numbers);
        total_sum = sum(numbers);
        average = total_sum / length;
    result = [length, total_sum, average];
    return result;

numbers = input("Enter a List of Integers Separated by Spaces: ");
result = analyze_list(numbers);

print(result);
print("Length:", result[0]);
print("Sum:", result[1]);
print("Average:", result[2]);