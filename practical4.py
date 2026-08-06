# ---------------------------String operations---------------------------

# Q1. Find length of function without len() function
# text = input("Enter a string: ")
# count = 0
# for i in text:
#     count = count + 1
# print("Length of the string is:", count)
# _________________________________________________-
# Q3. Reverse a string 
# text = input("Enter a string: ")
# for i in range(len(text) - 1, -1, -1):
#     print(text[i], end="")
# ----------------------------------------------------------
# Q.●	Count the number of vowels, consonants, digits, spaces, and special characters in a given string.  
# text = input("Enter a string: ")
# vowels = 0
# consonants = 0
# digits = 0
# spaces = 0
# special = 0

# for ch in text:
#     if ch in "aeiouAEIOU":
#         vowels += 1
#     elif ('a' <= ch <= 'z') or ('A' <= ch <= 'Z'):
#         consonants += 1
#     elif '0' <= ch <= '9':
#         digits += 1
#     elif ch == " ":
#         spaces += 1
#     else:
#         special += 1
# print("Vowels:", vowels)
# print("Consonants:", consonants)
# print("Digits:", digits)
# print("Spaces:", spaces)
# print("Special Characters:", special)

#Check if it is a palindrome or not 
# text = input("Enter a string: ")
# reverse = ""
# for i in range(len(text)-1, -1, -1):
#     reverse += text[i]
# if text == reverse:
#     print("Palindrome")
# else:
#     print("Not Palindrome")

# Uppercase lowercase count
# text = input("Enter a string: ")
# upper = 0
# lower = 0
# for ch in text:
#     if 'A' <= ch <= 'Z':
#         upper += 1
#     elif 'a' <= ch <= 'z':
#         lower += 1
# print("Uppercase:", upper)
# print("Lowercase:", lower)

# Replace characters
# text = input("Enter a string: ")
# old = input("Character to replace: ")
# new = input("New character: ")
# result = ""
# for ch in text:
#     if ch == old:
#         result += new
#     else:
#         result += ch
# print(result)

# remove spaces
# text = input("Enter a string: ")
# result = ""
# for ch in text:
#     if ch != " ":
#         result += ch
# print(result)

# print 1st and last character
# text = input("Enter a string: ")
# print("First Character:", text[0])
# print("Last Character:", text[len(text)-1])

 # ASCII values
# text = input("Enter a string: ")
# for ch in text:
#     print(ch, "=", ord(ch))

# word count
# text = input("Enter a sentence: ")
# count = 1
# for ch in text:
#     if ch == " ":
#         count += 1
# print("Total Words:", count)