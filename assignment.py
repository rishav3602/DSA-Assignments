"""
1. Write a Python program to reverse a string without using any built-in string reversal functions.
"""

def reverse_string(string):
    reversed_string = ""
    for i in range(len(string) - 1, -1, -1):
        reversed_string += string[i]
    return reversed_string

# Example usage
input_string = "Hello, World!"
reversed_string = reverse_string(input_string)
print(reversed_string)  # Output: "!dlroW ,olleH"


"""

2. Implement a function to check if a given string is a palindrome.
"""

def is_palindrome(string):
    reversed_string = reverse_string(string)
    if string.lower() == reversed_string.lower():
        return True
    else:
        return False

# Example usage
input_string = "level"
if is_palindrome(input_string):
    print("It's a palindrome!")
else:
    print("It's not a palindrome.")


"""
3. Write a program to find the largest element in a given list.
"""

def find_largest_element(lst):
    largest = lst[0]
    for num in lst:
        if num > largest:
            largest = num
    return largest

# Example usage
numbers = [4, 9, 2, 15, 7, 12]
largest_number = find_largest_element(numbers)
print(largest_number)  # Output: 15


"""
4. Implement a function to count the occurrence of each element in a list.
"""

def count_occurrences(lst):
    occurrence_count = {}
    for element in lst:
        if element in occurrence_count:
            occurrence_count[element] += 1
        else:
            occurrence_count[element] = 1
    return occurrence_count

# Example usage
numbers = [1, 2, 3, 2, 1, 3, 3, 4, 5, 4]
occurrences = count_occurrences(numbers)
print(occurrences)  # Output: {1: 2, 2: 2, 3: 3, 4: 2, 5: 1}


"""
5. Write a Python program to find the second largest number in a list.
"""

def find_second_largest(lst):
    largest = lst[0]
    second_largest = float('-inf')
    for num in lst:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num < largest:
            second_largest = num
    return second_largest

# Example usage
numbers = [4, 9, 2, 15, 7, 12]
second_largest_number = find_second_largest(numbers)
print(second_largest_number)  # Output: 12


"""
6. Implement a function to remove duplicate elements from a list.
"""

def remove_duplicates(lst):
    return list(set(lst))

# Example usage
numbers = [1, 2, 3, 2, 1, 3, 3, 4, 5, 4]
unique_numbers = remove_duplicates(numbers)
print(unique_numbers)  # Output: [1, 2, 3, 4, 5]


"""
7. Write a program to calculate the factorial of a given number.
"""

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Example usage
num = 5
result = factorial(num)
print(result)  # Output: 120


"""
8. Implement a function to check if a given number is prime.
"""

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Example usage
number = 17
if is_prime(number):
    print("It's a prime number!")
else:
    print("It's not a prime number.")


"""
9. Write a Python program to sort a list of integers in ascending order.
"""

def ascending_sort(lst):
    return sorted(lst)

# Example usage
numbers = [9, 3, 7, 1, 5]
sorted_numbers = ascending_sort(numbers)
print(sorted_numbers)  # Output: [1, 3, 5, 7, 9]


"""
10. Implement a function to find the sum of all numbers in a list.
"""

def find_sum(lst):
    total = 0
    for num in lst:
        total += num
    return total

# Example usage
numbers = [1, 2, 3, 4, 5]
sum_of_numbers = find_sum(numbers)
print(sum_of_numbers)  # Output: 15


"""
11. Write a program to find the common elements between two lists.
"""

def find_common_elements(list1, list2):
    common_elements = []
    for element in list1:
        if element in list2:
            common_elements.append(element)
    return common_elements

# Example usage
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common_elements = find_common_elements(list1, list2)
print(common_elements)  # Output: [4, 5]


"""
12. Implement a function to check if a given string is an anagram of another string.
"""

def is_anagram(string1, string2):
    return sorted(string1.lower()) == sorted(string2.lower())

# Example usage
word1 = "listen"
word2 = "silent"
if is_anagram(word1, word2):
    print("They are anagrams!")
else:
    print("They are not anagrams.")


"""
13. Write a Python program to generate all permutations of a given string.
"""

import itertools

def generate_permutations(string):
    permutations = list(itertools.permutations(string))
    return [''.join(permutation) for permutation in permutations]

# Example usage
input_string = "abc"
permutations = generate_permutations(input_string)
print(permutations)  # Output: ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']


"""
14. Implement a function to calculate the Fibonacci sequence up to a given number of terms.
"""

def fibonacci_sequence(n):
    sequence = [0, 1]
    while len(sequence) < n:
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)
    return sequence

# Example usage
terms = 10
fibonacci = fibonacci_sequence(terms)
print(fibonacci)  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


"""
15. Write a program to find the median of a list of numbers.
"""

def find_median(numbers):
    sorted_numbers = sorted(numbers)
    length = len(sorted_numbers)
    if length % 2 == 0:
        median = (sorted_numbers[length//2 - 1] + sorted_numbers[length//2]) / 2
    else:
        median = sorted_numbers[length//2]
    return median

# Example usage
numbers = [4, 2, 6, 8, 5, 1]
median = find_median(numbers)
print(median)  # Output: 4.5


"""
16. Implement a function to check if a given list is sorted in non-decreasing order.
"""

def is_sorted(lst):
    return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))

# Example usage
numbers = [1, 2, 3, 4, 5]
if is_sorted(numbers):
    print("The list is sorted!")
else:
    print("The list is not sorted.")


"""
17. Write a Python program to find the intersection of two lists.
"""

def find_intersection(list1, list2):
    intersection = list(set(list1) & set(list2))
    return intersection

# Example usage
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
intersection = find_intersection(list1, list2)
print(intersection)  # Output: [4, 5]


"""
18. Implement a function to find the maximum subarray sum in a given list.
"""

def max_subarray_sum(lst):
    max_sum = float('-inf')
    current_sum = 0
    for num in lst:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum

# Example usage
numbers = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
max_sum = max_subarray_sum(numbers)
print(max_sum)  # Output: 6


"""
19. Write a program to remove all vowels from a given string.
"""

def remove_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    return ''.join(char for char in string if char not in vowels)

# Example usage
input_string = "Hello, World!"
string_without_vowels = remove_vowels(input_string)
print(string_without_vowels)  # Output: "Hll, Wrld!"


"""
20. Implement a function to reverse the order of words in a given sentence.
"""

def reverse_words(sentence):
    words = sentence.split()
    reversed_sentence = ' '.join(words[::-1])
    return reversed_sentence

# Example usage
input_sentence = "Hello, World! Welcome to OpenAI."
reversed_sentence = reverse_words(input_sentence)
print(reversed_sentence)  # Output: "OpenAI. to Welcome World! Hello,"


"""
21. Write a Python program to check if two strings are anagrams of each other.
"""

def are_anagrams(string1, string2):
    return sorted(string1.lower()) == sorted(string2.lower())

# Example usage
word1 = "listen"
word2 = "silent"
if are_anagrams(word1, word2):
    print("They are anagrams!")
else:
    print("They are not anagrams.")


"""
22. Implement a function to find the first non-repeating character in a string.
"""

def find_first_non_repeating(string):
    char_count = {}
    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    for char in string:
        if char_count[char] == 1:
            return char
    return None

# Example usage
input_string = "aabbcdeff"
first_non_repeating = find_first_non_repeating(input_string)
print(first_non_repeating)  # Output: 'c'



"""
23. Write a program to find the prime factors of a given number.
"""

def find_prime_factors(number):
    prime_factors = []
    divisor = 2
    while divisor <= number:
        if number % divisor == 0:
            prime_factors.append(divisor)
            number = number // divisor
        else:
            divisor += 1
    return prime_factors

# Example usage
num = 24
prime_factors = find_prime_factors(num)
print(prime_factors)  # Output: [2, 2, 2, 3]


"""
24. Implement a function to check if a given number is a power of two.
"""

def is_power_of_two(number):
    if number <= 0:
        return False
    while number > 1:
        if number % 2 != 0:
            return False
        number = number // 2
    return True

# Example usage
num = 16
if is_power_of_two(num):
    print("It's a power of two!")
else:
    print("It's not a power of two.")


"""
25. Write a Python program to merge two sorted lists into a single sorted list.
"""

def merge_sorted_lists(list1, list2):
    merged_list = []
    i, j = 0, 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1
    merged_list.extend(list1[i:])
    merged_list.extend(list2[j:])
    return merged_list

# Example usage
list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]
merged = merge_sorted_lists(list1, list2)
print(merged)  # Output: [1, 2, 3, 4, 5, 6, 7, 8]


"""
26. Implement a function to find the mode of a list of numbers.
"""

from collections import Counter

def find_mode(numbers):
    count = Counter(numbers)
    max_count = max(count.values())
    mode = [num for num, freq in count.items() if freq == max_count]
    return mode

# Example usage
numbers = [1, 2, 3, 2, 1, 3, 3, 4, 5, 4]
modes = find_mode(numbers)
print(modes)  # Output: [3]


"""
27. Write a program to find the greatest common divisor (GCD) of two numbers.
"""

def find_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Example usage
num1 = 48
num2 = 60
gcd = find_gcd(num1, num2)
print(gcd)  # Output: 12


"""
28. Implement a function to calculate the square root of a given number.
"""

def calculate_square_root(num):
    return num ** 0.5

# Example usage
number = 16
square_root = calculate_square_root(number)
print(square_root)  # Output: 4.0


"""
29. Write a Python program to check if a given string is a valid palindrome ignoring non-alphanumeric characters.
"""

import re

def is_valid_palindrome(string):
    alphanumeric_string = re.sub(r'\W+', '', string)
    reversed_string = alphanumeric_string[::-1]
    return alphanumeric_string.lower() == reversed_string.lower()

# Example usage
input_string = "A man, a plan, a canal: Panama!"
if is_valid_palindrome(input_string):
    print("It's a valid palindrome!")
else:
    print("It's not a valid palindrome.")


"""
30. Implement a function to find the minimum element in a rotated sorted list.
"""

def find_min_element_rotated_sorted(lst):
    left, right = 0, len(lst) - 1
    while left < right:
        mid = left + (right - left) // 2
        if lst[mid] > lst[right]:
            left = mid + 1
        else:
            right = mid
    return lst[left]

# Example usage
numbers = [4, 5, 6, 7, 0, 1, 2]
min_element = find_min_element_rotated_sorted(numbers)
print(min_element)  # Output: 0


"""
31. Write a program to find the sum of all even numbers in a list.
"""

def sum_even_numbers(lst):
    return sum(num for num in lst if num % 2 == 0)

# Example usage
numbers = [1, 2, 3, 4, 5, 6]
sum_even = sum_even_numbers(numbers)
print(sum_even)  # Output: 12


"""
32. Implement a function to calculate the power of a number using recursion.
"""

def power(base, exponent):
    if exponent == 0:
        return 1
    elif exponent < 0:
        return 1 / power(base, -exponent)
    else:
        return base * power(base, exponent - 1)

# Example usage
base = 2
exponent = 3
result = power(base, exponent)
print(result)  # Output: 8


"""
33. Write a Python program to remove duplicates from a list while preserving the order.
"""

def remove_duplicates_preserve_order(lst):
    unique_list = []
    for element in lst:
        if element not in unique_list:
            unique_list.append(element)
    return unique_list

# Example usage
numbers = [1, 2, 3, 2, 1, 3, 3, 4, 5, 4]
unique_numbers = remove_duplicates_preserve_order(numbers)
print(unique_numbers)  # Output: [1, 2, 3, 4, 5]


"""
34. Implement a function to find the longest common prefix among a list of strings.
"""

def find_longest_common_prefix(strings):
    if not strings:
        return ""
    min_length = min(len(string) for string in strings)
    prefix = ""
    for i in range(min_length):
        if all(string[i] == strings[0][i] for string in strings):
            prefix += strings[0][i]
        else:
            break
    return prefix

# Example usage
words = ["flower", "flow", "flight"]
common_prefix = find_longest_common_prefix(words)
print(common_prefix)  # Output: "fl"


"""
35. Write a program to check if a given number is a perfect square.
"""

def is_perfect_square(num):
    if num < 0:
        return False
    sqrt = int(num ** 0.5)
    return sqrt * sqrt == num

# Example usage
number = 16
if is_perfect_square(number):
    print("It's a perfect square!")
else:
    print("It's not a perfect square.")


"""
36. Implement a function to calculate the product of all elements in a list.
"""


def calculate_product(lst):
    product = 1
    for num in lst:
        product *= num
    return product

# Example usage
numbers = [2, 3, 4, 5]
product = calculate_product(numbers)
print(product)  # Output: 120

"""
37. Write a Python program to reverse the order of words in a sentence while preserving the word order.
"""

def reverse_words_preserve_order(sentence):
    words = sentence.split()
    reversed_sentence = ' '.join(words[::-1])
    return reversed_sentence

# Example usage
input_sentence = "Hello, World! Welcome to OpenAI."
reversed_sentence = reverse_words_preserve_order(input_sentence)
print(reversed_sentence)  # Output: "OpenAI. to Welcome World! Hello,"


"""
38. Implement a function to find the missing number in a given list of consecutive numbers.
"""

def find_missing_number(lst):
    n = len(lst) + 1
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(lst)
    return expected_sum - actual_sum

# Example usage
numbers = [1, 2, 3, 5]
missing_number = find_missing_number(numbers)
print(missing_number)  # Output: 4


"""
39. Write a program to find the sum of digits of a given number.
"""

def sum_of_digits(number):
    total = 0
    while number > 0:
        total += number % 10
        number //= 10
    return total

# Example usage
num = 12345
digit_sum = sum_of_digits(num)
print(digit_sum)


"""
40. Implement a function to check if a given string is a valid palindrome considering case sensitivity.
"""
def is_valid_palindrome_case_sensitive(string):
    return string == string[::-1]

# Example usage
input_string = "Madam"
if is_valid_palindrome_case_sensitive(input_string):
    print("It's a valid palindrome!")
else:
    print("It's not a valid palindrome.")


"""
41. Write a Python program to find the smallest missing positive integer in a list.
"""
def find_smallest_missing_positive(lst):
    positive_numbers = set([num for num in lst if num > 0])
    smallest_positive = 1
    while smallest_positive in positive_numbers:
        smallest_positive += 1
    return smallest_positive

# Example usage
numbers = [3, 4, -1, 1]
smallest_missing = find_smallest_missing_positive(numbers)
print(smallest_missing)  # Output: 2


"""
42. Implement a function to find the longest palindrome substring in a given string.
"""
def find_longest_palindrome_substring(string):
    longest_substring = ""
    for i in range(len(string)):
        for j in range(i, len(string)):
            substring = string[i:j+1]
            if substring == substring[::-1] and len(substring) > len(longest_substring):
                longest_substring = substring
    return longest_substring

# Example usage
input_string = "babad"
longest_palindrome = find_longest_palindrome_substring(input_string)
print(longest_palindrome)  # Output: "bab"


"""
43. Write a program to find the number of occurrences of a given element in a list.
"""

def count_occurrences(lst, element):
    return lst.count(element)

# Example usage
numbers = [1, 2, 3, 2, 1, 3, 3, 4, 5, 4]
element = 3
occurrences = count_occurrences(numbers, element)
print(occurrences)  # Output: 3


"""
44. Implement a function to check if a given number is a perfect number.
"""

def is_perfect_number(number):
    divisors = [i for i in range(1, number) if number % i == 0]
    return sum(divisors) == number

# Example usage
num = 28
if is_perfect_number(num):
    print("It's a perfect number!")
else:
    print("It's not a perfect number.")


"""
45. Write a Python program to remove all duplicates from a string.
"""
def remove_duplicates_from_string(string):
    return ''.join(set(string))

# Example usage
input_string = "Hello, World!"
string_without_duplicates = remove_duplicates_from_string(input_string)
print(string_without_duplicates)  # Output: " ,oHleWrd!"


"""
46. Implement a function to find the first missing positive
"""
def find_first_missing_positive(lst):
    n = len(lst)
    for i in range(n):
        while 1 <= lst[i] <= n and lst[i] != lst[lst[i] - 1]:
            lst[lst[i] - 1], lst[i] = lst[i], lst[lst[i] - 1]
    for i in range(n):
        if lst[i] != i + 1:
            return i + 1
    return n + 1

# Example usage
numbers = [





