# Program 1
# Write a Python Program to print "Hello World".

print("Hello World!")



# Program 2
# Write a Python Program to take user input and display it.

Data = input("Enter Your Name: ")
print(Data)



# Program 3
# Write a Python Program to swap two numbers.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
a, b = b, a
print("After swapping:")
print("a =", a)
print("b =", b)



# Program 4
# Write a Python Program to check if a number is even or odd.

num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")
    
       
    
# Program 5
# Write a Python Program to find the largest of three numbers.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
print("Largest number is:", max(a, b, c))



# Program 6
# Write a Python Program to calculate the factorial of a number.

n = int(input("Enter a number: "))
fact = 1
for i in range(1, n + 1):
    fact = fact * i
print("Factorial is:", fact)



# Program 7
# Write a Python Program to generate the Fibonacci series.

n = int(input("Enter number of terms: "))
a, b = 0, 1
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
print()



# Program 8
# Write a Python Program to reverse a number.

num = input("Enter a number: ")
print("Reversed number:", num[::-1])



# Program 9
# Write a Python Program to check if a number is prime.

num = int(input("Enter a number: "))
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")
else:
    print("Not Prime")
    
    
    
# Program 10
# Write a Python Program to find the sum of digits of a number.

num = input("Enter a number: ")
total = 0
for digit in num:
    total += int(digit)
print("Sum of digits:", total)



# Program 11
# Write a Python Program to reverse a string.

s = input("Enter a string: ")
print("Reversed string:", s[::-1])



# Program 12
# Write a Python Program to check if a string is a palindrome.

s = input("Enter a string: ")
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
    
    
    
# Program 13
# Write a Python Program to count vowels and consonants in a string.

s = input("Enter a string: ").lower()
vowels = "aeiou"
v = 0
c = 0
for ch in s:
    if ch.isalpha():
        if ch in vowels:
            v += 1
        else:
            c += 1
print("Vowels:", v)
print("Consonants:", c)



# Program 14
# Write a Python Program to find the length of a string without using 'len().

s = input("Enter a string: ")
count = 0
for ch in s:
    count += 1
print("Length of string:", count)




# Program 15
# Write a Python Program to remove all spaces from a string.

s = input("Enter a string: ")
print("String without spaces:", s.replace(" ", ""))



# Program 16
# Write a Python Program to count occurrences of a substring.

s = input("Enter a string: ")
sub = input("Enter substring: ")
print("Occurrences:", s.count(sub))



# Program 17
# Write a Python Program to convert a string to uppercase.

s = input("Enter a string: ")
print("Uppercase:", s.upper())



# Program 18
# Write a Python Program to replace vowels with '*'.

s = input("Enter a string: ")
vowels = "aeiouAEIOU"
for v in vowels:
    s = s.replace(v, "*")
print("Modified string:", s)



# Program 19
# Write a Python Program to check if two strings are anagrams.

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
if sorted(s1) == sorted(s2):
    print("Anagrams")
else:
    print("Not Anagrams")
    
    
    
# Program 20
# Write a Python Program to find the first non-repeated character in a string.

s = input("Enter a string: ")
for ch in s:
    if s.count(ch) == 1:
        print("First non-repeated character:", ch)
        break
    
    
    
# Program 21
# Write a Python Program to find the largest element in a list.

lst = [10, 30, 56, 78]
print("Largest element:", max(lst))



# Program 22
# Write a Python Program to find the smallest element in a list.

lst = [10,34,68,89,12]
print("Smallest element:", min(lst))



# Program 23
# Write a Python Program to calculate the sum of elements in a list.

lst = [10, 23, 47, 28, 00]
print("Sum of elements:", sum(lst))



# Program 24
# Write a Python Program to remove duplicates from a list.

lst = [20,34,54,66]
print("List without duplicates:", list(set(lst)))



# Program 25
# Write a Python Program to sort a list in ascending order.

lst = [13,44,55,21,54]
lst.sort()
print("Sorted list:", lst)



# Program 26
# Write a Python Program to sort a list in descending order.

lst = [13,44,55,21,54]
lst.sort(reverse=True)
print("Sorted list (descending):", lst)


# Program 27
# Write a Python Program to find the second largest element in a list.

lst = [13,44,55,21,54]
lst = list(set(lst))
lst.sort()
print("Second largest element:", lst[-2])



# Program 28
# Write a Python Program to merge two lists.

list1 = [13,44,55,21,54]
list2 = [1,2,3,5,6]
merged = list1 + list2
print("Merged list:", merged)



# Program 29
# Write a Python Program to find common elements between two lists.

list1 = [13,44,55,21,54]
list2 = [44,21,54,56]
common = list(set(list1) & set(list2))
print("Common elements:", common)



# Program 30
# Write a Python Program to rotate a list by 'k' positions.

lst = [13,44,55,21,54]
k = int(input("Enter k: "))
k = k % len(lst)
rotated = lst[k:] + lst[:k]
print("Rotated list:", rotated)



# Program 31
# Write a Python Program to check if a number is an Armstrong number.

num = int(input("Enter a number: "))
temp = num
digits = len(str(num))
total = 0
while temp > 0:
    d = temp % 10
    total += d ** digits
    temp //= 10
if total == num:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
    
    
    
# Program 32
# Write a Python Program to check if a number is a perfect number.

num = int(input("Enter a number: "))
sum_div = 0
for i in range(1, num):
    if num % i == 0:
        sum_div += i
if sum_div == num:
    print("Perfect number")
else:
    print("Not a perfect number")
    
    
    
# Program 33
# Write a Python Program to check if a number is a palindrome.

num = input("Enter a number: ")
if num == num[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")



# Program 34
# Write a Python Program to find the GCD of two numbers.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
while b != 0:
    a, b = b, a % b
print("GCD is:", a)



# Program 35
# Write a Python Program to find the LCM of two numbers.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
x, y = a, b
while y:
    x, y = y, x % y
gcd = x
lcm = (a * b) // gcd
print("LCM is:", lcm)



# Program 36
# Write a Python Program to convert decimal to binary.

num = int(input("Enter a decimal number: "))
print("Binary:", bin(num)[2:])



# Program 37
# Write a Python Program to convert binary to decimal.

binary = input("Enter a binary number: ")
decimal = int(binary, 2)
print("Decimal:", decimal)



# Program 38
# Write a Python Program to generate prime numbers up to 'n'.

n = int(input("Enter n: "))
for num in range(2, n + 1):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num, end=" ")
print()



# Program 39
# Write a Python Program to find the sum of natural numbers up to 'n

n = int(input("Enter n: "))
total = 0
for i in range(1, n + 1):
    total += i

print("Sum:", total)



# Program 40
# Write a Python Program to calculate the power of a number without using '**'.

base = int(input("Enter base: "))
exp = int(input("Enter exponent: "))
result = 1
for i in range(exp):
    result *= base
print("Result:", result)



# Program 41
# Write a Python Program to read a text file.

file = open("sample.txt", "r")
print(file.read())
file.close()



# Program 42
# Write a Python Program to write to a text file.

file = open("sample.txt", "w")
file.write("This is a sample text file.")
file.close()
print("Data written to file")



# Program 43
# Write a Python Program to count words in a file.

file = open("sample.txt", "r")
words = file.read().split()
print("Word count:", len(words))
file.close()



# Program 44
# Write a Python Program to count lines in a file.

file = open("sample.txt", "r")
lines = file.readlines()
print("Line count:", len(lines))
file.close()



# Program 45
# Write a Python Program to copy contents from one file to another.

src = open("sample.txt", "r")
dest = open("copy.txt", "w")
dest.write(src.read())
src.close()
dest.close()
print("File copied")



# Program 46
# Write a Python Program to check if a file exists.

import os
filename = "sample.txt"
if os.path.exists(filename):
    print("File exists")
else:
    print("File does not exist")



# Program 47
# Write a Python Program to append text to a file.

file = open("sample.txt", "a")
file.write("\nAppended text.")
file.close()
print("Text appended")



# Program 48
# Write a Python Program to find the longest word in a file.

file = open("sample.txt", "r")
words = file.read().split()
longest = max(words, key=len)
print("Longest word:", longest)
file.close()



# Program 49
# Write a Python Program to remove blank lines from a file.

file = open("sample.txt", "r")
lines = file.readlines()
file.close()
file = open("sample.txt", "w")
for line in lines:
    if line.strip():
        file.write(line)
file.close()
print("Blank lines removed")



# Program 50
# Write a Python Program to read a CSV file.

import csv
with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)



