# Program 101
# Write a Python Program to iterate over a list using 'for' loop.

my_list = [10, 20, 30, 40]
for item in my_list:
    print(item)



# Program 102
# Write a Python Program to iterate over a list using 'while' loop.

my_list = [10, 20, 30, 40]
i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1
    
    
    
# Program 103
# Write a Python Program to find the sum of elements in a tuple.

my_tuple = (1, 2, 3, 4)
print("Sum:", sum(my_tuple))



# Program 104
# Write a Python Program to check if an element exists in a tuple.

my_tuple = (10, 20, 30)
key = int(input("Enter element: "))
if key in my_tuple:
    print("Element exists")
else:
    print("Element does not exist")



# Program 105
# Write a Python Program to convert a string into a list of characters.

text = input("Enter a string: ")
char_list = list(text)
print("Character list:", char_list)



# Program 106
# Write a Python Program to join a list of strings into a single string.

words = ["Hello", "World", "Python"]
sentence = " ".join(words)
print("Sentence:", sentence)



# Program 107
# Write a Python Program to find the largest word in a sentence.

sentence = input("Enter a sentence: ")
words = sentence.split()
largest = max(words, key=len)
print("Largest word:", largest)



# Program 108
# Write a Python Program to find the smallest word in a sentence.

sentence = input("Enter a sentence: ")
words = sentence.split()
smallest = min(words, key=len)
print("Smallest word:", smallest)



# Program 109
# Write a Python Program to count the number of words in a sentence.

sentence = input("Enter a sentence: ")
words = sentence.split()
print("Number of words:", len(words))



# Program 110
# Write a Python Program to check if a number is positive, negative, or zero.

num = int(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")



# Program 111
# Write a Python Program to check if a year is a leap year.

year = int(input("Enter year: "))
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not a Leap Year")
    
    
    
# Program 112
# Write a Python Program to calculate simple interest.

p = float(input("Enter principal: "))
r = float(input("Enter rate: "))
t = float(input("Enter time: "))
si = (p * r * t) / 100
print("Simple Interest:", si)



# Program 113
# Write a Python Program to calculate compound interest.

p = float(input("Enter principal: "))
r = float(input("Enter rate: "))
t = float(input("Enter time: "))
ci = p * ((1 + r / 100) ** t) - p
print("Compound Interest:", ci)



# Program 114
# Write a Python Program to convert Celsius to Fahrenheit.

celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9 / 5) + 32
print("Fahrenheit:", fahrenheit)



# Program 115
# Write a Python Program to convert Fahrenheit to Celsius.

fahrenheit = float(input("Enter temperature in Fahrenheit: "))
celsius = (fahrenheit - 32) * 5 / 9
print("Celsius:", celsius)



# Program 116
# Write a Python Program to calculate area of a circle.

import math
radius = float(input("Enter radius: "))
area = math.pi * radius * radius
print("Area of circle:", area)



# Program 117
# Write a Python Program to calculate area of a rectangle

length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))
area = length * breadth
print("Area of rectangle:", area)



# Program 118
# Write a Python Program to calculate area of a triangle.

base = float(input("Enter base: "))
height = float(input("Enter height: "))
area = 0.5 * base * height
print("Area of triangle:", area)



# Program 119
# Write a Python Program to calculate perimeter of a square.

side = float(input("Enter side: "))
perimeter = 4 * side
print("Perimeter of square:", perimeter)



# Program 120
# Write a Python Program to calculate perimeter of a rectangle.

length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))
perimeter = 2 * (length + breadth)
print("Perimeter of rectangle:", perimeter)



# Program 121
# Write a Python Program to calculate perimeter of a circle.

radius = float(input("Enter radius: "))
perimeter = 2 * math.pi * radius
print("Perimeter of circle:", perimeter)



# Program 122
# Write a Python Program to calculate volume of a cube.

side = float(input("Enter side: "))
volume = side ** 3
print("Volume of cube:", volume)



# Program 123
# Write a Python Program to calculate volume of a cylinder.

radius = float(input("Enter radius: "))
height = float(input("Enter height: "))
volume = math.pi * radius * radius * height
print("Volume of cylinder:", volume)



# Program 124
# Write a Python Program to calculate volume of a sphere.

radius = float(input("Enter radius: "))
volume = (4 / 3) * math.pi * radius ** 3
print("Volume of sphere:", volume)



# Program 125
# Write a Python Program to calculate surface area of a cube.

side = float(input("Enter side: "))
surface_area = 6 * side * side
print("Surface area of cube:", surface_area)



# Program 126
# Write a Python Program to calculate surface area of a cylinder.

import math
radius = float(input("Enter radius: "))
height = float(input("Enter height: "))
surface_area = 2 * math.pi * radius * (radius + height)
print("Surface area of cylinder:", surface_area)



# Program 127
# Write a Python Program to calculate surface area of a sphere.

radius = float(input("Enter radius: "))
surface_area = 4 * math.pi * radius ** 2
print("Surface area of sphere:", surface_area)



# Program 128
# Write a Python Program to check if a character is uppercase.

ch = input("Enter a character: ")
if ch.isupper():
    print("Uppercase letter")
else:
    print("Not an uppercase letter")
    
    
    
# Program 129
# Write a Python Program to check if a character is lowercase.

ch = input("Enter a character: ")
if ch.islower():
    print("Lowercase letter")
else:
    print("Not a lowercase letter")
    
    
    
# Program 130
# Write a Python Program to check if a character is a digit.

ch = input("Enter a character: ")
if ch.isdigit():
    print("Digit")
else:
    print("Not a digit")
    
    
    
# Program 131
# Write a Python Program to check if a character is an alphabet.

ch = input("Enter a character: ")
if ch.isalpha():
    print("Alphabet")
else:
    print("Not an alphabet")



# Program 132
# Write a Python Program to check if a character is a special symbol.

ch = input("Enter a character: ")
if not ch.isalnum():
    print("Special symbol")
else:
    print("Not a special symbol")
    
    
    
# Program 133
# Write a Python Program to count uppercase letters in a string.

text = input("Enter a string: ")
count = 0
for ch in text:
    if ch.isupper():
        count += 1
print("Uppercase letters count:", count)



# Program 134
# Write a Python Program to count lowercase letters in a string

text = input("Enter a string: ")
count = 0
for ch in text:
    if ch.islower():
        count += 1
print("Lowercase letters count:", count)



# Program 135
# Write a Python Program to count digits in a string

text = input("Enter a string: ")
count = 0
for ch in text:
    if ch.isdigit():
        count += 1
print("Digits count:", count)



# Program 136
# Write a Python Program to count special characters in a string.

text = input("Enter a string: ")
count = 0
for ch in text:
    if not ch.isalnum():
        count += 1
print("Special characters count:", count)



# Program 137
# Write a Python Program to remove punctuation from a string.

import string
text = input("Enter a string: ")
result = ""
for ch in text:
    if ch not in string.punctuation:
        result += ch
print("Without punctuation:", result)



# Program 138
# Write a Python Program to replace spaces with hyphens in a string.

text = input("Enter a string: ")
print(text.replace(" ", "-"))



# Program 139
# Write a Python Program to split a string into words.

text = input("Enter a string: ")
words = text.split()
print("Words:", words)



# Program 140
# Write a Python Program to join words into a sentence.

words = ["Python", "is", "easy"]
sentence = " ".join(words)
print(sentence)



# Program 141
# Write a Python Program to check if a number is divisible by another number.

num = int(input("Enter number: "))
div = int(input("Enter divisor: "))
if num % div == 0:
    print("Divisible")
else:
    print("Not divisible")
    
    
    
# Program 142
# Write a Python Program to find the square root of a number.

num = float(input("Enter number: "))
print("Square root:", math.sqrt(num))



# Program 143
# Write a Python Program to find cube root of a number.

num = float(input("Enter number: "))
print("Cube root:", num ** (1/3))



# Program 144
# Write a Python Program to calculate power using pow() function

base = int(input("Enter base: "))
exp = int(input("Enter exponent: "))
print("Result:", pow(base, exp))



# Program 145
# Write a Python Program to calculate absolute value of a number.

num = int(input("Enter number: "))
print("Absolute value:", abs(num))



# Program 146
# Write a Python Program to generate random numbers.

import random
print("Random number:", random.random())



# Program 147
# Write a Python Program to generate random integers between two numbers.

start = int(input("Enter start: "))
end = int(input("Enter end: "))
print("Random integer:", random.randint(start, end))



# Program 148
# Write a Python Program to shuffle elements of a list.

import random
my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list)
print("Shuffled list:", my_list)



# Program 149
# Write a Python Program to pick a random element from a list

my_list = ["apple", "banana", "cherry"]
print("Random element:", random.choice(my_list))



# Program 150
# Write a Python Program to simulate rolling a dice

dice = random.randint(1, 6)
print("Dice rolled:", dice)