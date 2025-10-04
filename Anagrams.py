# Q1. Write a Python program to check if two strings are anagrams of each other.

# Function to check if two strings are anagrams
def is_anagrams(str1,str2):
    # Remove the spaces and convert both the strings to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Sort the characters of both strings and compare
    return sorted(str1) == sorted(str2)

# Main Program
# Taking input from the user
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

# Checking if the strings are anagrams
if is_anagrams(str1, str2):
    print(f"'{str1}' and '{str2}' are anagrams of each other.")
else:
    print(f"'{str1}' and '{str2}' are not anagrams of each other.")
