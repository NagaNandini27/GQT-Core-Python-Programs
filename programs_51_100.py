# Program 51
# Write a Python Program to print multiplication table of a number.

num = int(input("Enter a number: "))
for i in range(1, 11):
    print(num, "x", i, "=", num * i)



# Program 52
# Write a Python Program to print all even numbers between 1 and 100.

for i in range(2, 101, 2):
    print(i, end=" ")
print()



# Program 53
# Write a Python Program to print all odd numbers between 1 and 100.

for i in range(1, 100, 2):
    print(i, end=" ")
print()



# Program 54
# Write a Python Program to calculate the sum of first 'n' natural numbers using a loop.

n = int(input("Enter n: "))
total = 0
for i in range(1, n + 1):
    total += i
print("Sum:", total)



# Program 55
# Write a Python Program to print a pyramid pattern of stars.

n = int(input("Enter number of rows: "))
for i in range(1, n + 1):
    for k in range(n-i+1):
        print(' ',end=' ')
    for j in range(2*i-1):
        print('*', end=' ')
    print()
    
    
    
# Program 56
# Write a Python Program to print an inverted pyramid of stars.

n = int(input("Enter number of rows: "))
for i in range(1, n+1):
    for k in range(1,i+1):
        print(' ',end=' ')
    for j in range(2*(n-i)+1):
        print('*', end=' ')
    print()
    
    
    
# Program 57
# Write a Python Program to print Pascal's triangle.

n = int(input("Enter number of rows: "))
for i in range(n):
    num = 1
    print(" " * (n - i), end="")
    for j in range(i + 1):
        print(num, end=" ")
        num = num * (i - j) // (j + 1)
    print()
    
    
    
# Program 58
# Write a Python Program to print Floyd's triangle.

n = int(input("Enter number of rows: "))
count = 1
for i in range(1, n + 1):
    for j in range(1, i+1):
        print(count, end=" ")
        count = count+1
    print()
    
    
    
# Program 59
# Write a Python Program to print prime numbers between 1 and 100.

for num in range(2, 101):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num, end=" ")
print()



# Program 60
# Write a Python Program to print numbers divisible by 3 and 5 up to 100.

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print(i, end=" ")
print()



# Program 61
# Write a Python Program to define a function that returns the square of a number.

def square(n):
    return n * n
num = int(input("Enter a number: "))
print("Square:", square(num))



# Program 62
# Write a Python Program to define a function that checks if a number is prime.

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
num = int(input("Enter a number: "))
print("Prime" if is_prime(num) else "Not Prime")



# Program 63
# Write a Python Program to define a function that calculates factorial using recursion.

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
num = int(input("Enter a number: "))
print("Factorial:", factorial(num))



# Program 64
# Write a Python Program to define a function that finds the maximum of three numbers.

def max_of_three(a, b, c):
    return max(a, b, c)
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
print("Maximum:", max_of_three(a, b, c))



# Program 65
# Write a Python Program to define a function that returns the reverse of a string.

def reverse_string(s):
    return s[::-1]
s = input("Enter a string: ")
print("Reversed:", reverse_string(s))



# Program 66
# Write a Python Program to define a function that counts vowels in a string

def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in s:
        if ch in vowels:
            count += 1
    return count
s = input("Enter a string: ")
print("Vowel count:", count_vowels(s))



# Program 67
# Write a Python Program to define a function that checks if a string is palindrome.

def is_palindrome(s):
    return s == s[::-1]
s = input("Enter a string: ")
print("Palindrome" if is_palindrome(s) else "Not Palindrome")



# Program 68
# Write a Python Program to define a function that returns the sum of digits of a number.

def sum_of_digits(n):
    total = 0
    for d in str(n):
        total += int(d)
    return total
num = int(input("Enter a number: "))
print("Sum of digits:", sum_of_digits(num))



# Program 69
# Write a Python Program to define a function that generates Fibonacci series up to 'n'.

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()
n = int(input("Enter number of terms: "))
fibonacci(n)



# Program 70
# Write a Python Program to define a function that calculates power of a number using recursion.

def power(base, exp):
    if exp == 0:
        return 1
    return base * power(base, exp - 1)
base = int(input("Enter base: "))
exp = int(input("Enter exponent: "))
print("Result:", power(base, exp))



# Program 71
# Write a Python Program to calculate factorial using recursion.

def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)
num = int(input("Enter a number: "))
print("Factorial:", fact(num))



# Program 72
# Write a Python Program to generate Fibonacci series using recursion.

def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)
n = int(input("Enter number of terms: "))
for i in range(n):
    print(fib(i), end=" ")
print()



# Program 73
# Write a Python Program to find the sum of natural numbers using recursion.

def sum_n(n):
    if n == 0:
        return 0
    return n + sum_n(n - 1)
n = int(input("Enter n: "))
print("Sum:", sum_n(n))



# Program 74
# Write a Python Program to reverse a string using recursion.

def reverse_rec(s):
    if s == "":
        return s
    return reverse_rec(s[1:]) + s[0]
s = input("Enter a string: ")
print("Reversed:", reverse_rec(s))



# Program 75
# Write a Python Program to check if a string is palindrome using recursion

def palindrome_rec(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return palindrome_rec(s[1:-1])
s = input("Enter a string: ")
print("Palindrome" if palindrome_rec(s) else "Not Palindrome")



# Program 76
# Write a Python Program to find GCD of two numbers using recursion.

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("GCD:", gcd(a, b))



# Program 77
# Write a Python Program to find LCM of two numbers using recursion.

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
lcm = (a * b) // gcd(a, b)
print("LCM:", lcm)



# Program 78
# Write a Python Program to calculate sum of digits using recursion.

def sum_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_digits(n // 10)
num = int(input("Enter number: "))
print("Sum of digits:", sum_digits(num))



# Program 79
# Write a Python Program to find the length of a string using recursion.

def string_length(s):
    if s == "":
        return 0
    return 1 + string_length(s[1:])
text = input("Enter string: ")
print("Length:", string_length(text))



# Program 80
# Write a Python Program to print numbers from 'n' to 1 using recursion.

def print_numbers(n):
    if n == 0:
        return
    print(n)
    print_numbers(n - 1)
n = int(input("Enter number: "))
print_numbers(n)



# Program 81
# Write a Python Program to find the maximum element in a tuple.

t = (10, 25, 5, 40, 15)
print("Maximum element:", max(t))



# Program 82
# Write a Python Program to find the minimum element in a tuple.

t = (10, 25, 5, 40, 15)
print("Minimum element:", min(t))



# Program 83
# Write a Python Program to convert a list into a tuple.

lst = [1, 2, 3, 4]
tup = tuple(lst)
print("Tuple:", tup)



# Program 84
# Write a Python Program to convert a tuple into a list.

tup = (1, 2, 3, 4)
lst = list(tup)
print("List:", lst)



# Program 85
# Write a Python Program to find the union of two sets.

set1 = {1, 2, 3}
set2 = {3, 4, 5}
print("Union:", set1 | set2)



# Program 86
# Write a Python Program to find the intersection of two sets.

set1 = {1, 2, 3}
set2 = {3, 4, 5}
print("Intersection:", set1 & set2)



# Program 87
# Write a Python Program to find the difference of two sets.

set1 = {1, 2, 3}
set2 = {3, 4, 5}
print("Difference:", set1 - set2)



# Program 88
# Write a Python Program to check if a set is subset of another set.

set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = {1, 2}
print("Is subset:", set3.issubset(set1))



# Program 89
# Write a Python Program to remove duplicates from a list using set.

lst = [1, 2, 2, 3, 4, 4, 5]
unique = list(set(lst))
print("List without duplicates:", unique)



# Program 90
# Write a Python Program to count unique elements in a list using set.

lst = [1, 2, 2, 3, 3, 4]
print("Unique elements count:", len(set(lst)))



# Program 91
# Write a Python Program to create a dictionary of student names and marks.

students = {"Alice": 85, "Bob": 90, "Charlie": 78}
print(students)



# Program 92
# Write a Python Program to access values from a dictionary.

students = {"Alice": 85, "Bob": 90, "Charlie": 78}
print("Marks of Bob:", students["Bob"])



# Program 93
# Write a Python Program to update values in a dictionary.

students = {"Alice": 85, "Bob": 90, "Charlie": 78}
students["Alice"] = 88
print(students)



# Program 94
# Write a Python Program to delete a key from a dictionary

students = {"Alice": 85, "Bob": 90, "Charlie": 78}
del students["Charlie"]
print(students)



# Program 95
# Write a Python Program to merge two dictionaries.

dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged = {**dict1, **dict2}
print("Merged dictionary:", merged)



# Program 96
# Write a Python Program to count frequency of characters in a string using dictionary.

text = input("Enter string: ")
freq = {}
for ch in text:
    freq[ch] = freq.get(ch, 0) + 1
print(freq)



# Program 97
# Write a Python Program to count frequency of words in a sentence using dictionary.

sentence = input("Enter sentence: ")
words = sentence.split()
freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1
print(freq)



# Program 98
# Write a Python Program to find the key with maximum value in a dictionary.

data = {"a": 10, "b": 25, "c": 15}
print("Key with max value:", max(data, key=data.get))



# Program 99
# Write a Python Program to sort a dictionary by values.

data = {"a": 10, "b": 25, "c": 15}
sorted_dict = dict(sorted(data.items(), key=lambda x: x[1]))
print("Sorted dictionary:", sorted_dict)



# Program 100
# Write a Python Program to check if a key exists in a dictionary.

data = {"a": 10, "b": 25, "c": 15}
key = input("Enter key to check: ")
if key in data:
    print("Key exists")
else:
    print("Key does not exist")