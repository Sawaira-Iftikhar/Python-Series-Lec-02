"""
============================================
  LECTURE 2 - FILE 4: BOSS CHALLENGE 
  Topics: ALL 6 Topics Combined
  Total Challenges: 
============================================
  These problems combine Strings, Slicing,
  Methods, and Conditionals together.
============================================
"""

# ==========================================
#  CHALLENGE 1: The Palindrome Checker 🔤
#  Topics: Strings, Slicing, Conditionals
# ==========================================

 #-------------------Explanation-----------------
"""
 Write a program that:
1. Takes a word: word = "RaceCar"  (notice the mixed case!)
2. Converts it to lowercase
3. Reverses it using slicing
4. Checks if the original (lowered) equals the reversed
5. Prints the result using a conditional:

   If it IS a palindrome:
     "✅ 'racecar' is a palindrome!"
     "Original: racecar"
     "Reversed: racecar"
   If it is NOT:
     "❌ 'hello' is NOT a palindrome!"
     "Original: hello"
     "Reversed: olleh" 
"""

word = "RaceCar"

# Convert to lowercase
word = word.lower()
print("covert into lower: ", word)

#Reverse using slicing
reversed_word = word[::-1]
print("Reversed word: ", reversed_word)

# Checking if original and reversed are the same
if word == reversed_word:
    print( word, "is a palindrome!")
    print("Original: ",word)
    print("reversed: ",reversed_word)
else:
    print(word , "is Not a Palindrome!")
    print("Original: ", word)
    print("Reversed: ", reversed_word)

#-----------------------------------------------------------------------------------------

# ==========================================
#  CHALLENGE 2: The Password Validator 🔐
#  Topics: String Methods, len(), Conditionals, Logical Operators
# ==========================================

#----------------------Explanation-------------------------------------

"""
Write a password strength checker that validates a password
against these rules:

Rules:
  1. Length must be at least 8 characters
  2. Must contain at least one uppercase letter
  3. Must contain at least one lowercase letter
  4. Must contain at least one digit
  5. Must NOT contain spaces

Given: password = "MyP@ssw0rd"

Steps:
  a) Check each rule using string methods and conditionals
  b) Store each check as a boolean variable:
     - is_long_enough
     - has_upper
     - has_lower
     - has_digit
     - no_spaces
  c) Count how many rules pass
  d) Print a detailed report:

 """
# Password Strength Checker

password = "MyP@ssw0rd"

# Check each rule
long = len(password) >= 8
upper = password != password.lower()
lower = password != password.upper()
digit = any(char.isdigit() for char in password)
space = " " not in password

# Count how many rules passed
rules_passed = sum([long, upper, lower, digit, space])


# Print Detailed Report

print("==============================================")
print("            PASSWORD VALIDATOR                ")
print("==============================================")
print("Password: ",password)
print("----------------------------------------------")
print(f"Length >= 8:           {'Pass' if long else 'Fail'} ({len(password)} chars)")
print(f"Has Uppercase letters: {'Pass' if upper else 'Fail'}")
print(f"Has Lowercase letters: {'Pass' if lower else 'Fail'}")
print(f"Has Digits:            {'Pass' if digit else 'Fail'}")
print(f"Has  no Spaces:        {'Pass' if space else 'Fail'}")
print("----------------------------------------------")
print(f"Rules passed: {rules_passed/5}")

# Determine password strength 
if rules_passed== 5:
    print("Verdict: Strong Password!")
elif rules_passed >= 3:
    print("Verdict: Medium Passwrod")
elif rules_passed >= 1:
    print("Verdict: Weak Password")
else:
    print("Verdict: Very WEak Password")

print("==============================================")

#-----------------------------------------------------------------------------------------

# ==========================================
#  CHALLENGE 3: The Text Analyzer 📊
#  Topics: ALL — Strings, Indexing, Slicing, Methods, Conditionals
# ==========================================

#------------------------Explanation-----------------------------
"""
Write a program that analyzes a given sentence and prints
a detailed report.

Given: text = "  Python is an AMAZING programming language!  "

Your program should:
1. Clean the text (strip whitespace)
2. Print the cleaned text
3. Print the total number of characters
4. Print the first and last character using indexing
5. Print the first word and last word using slicing/split
6. Count how many times the letter "a" appears (case-insensitive)
7. Check if the text contains the word "AMAZING"
8. Replace "AMAZING" with "awesome" (lowercase)
9. Convert the entire text to title case
10. Check if the cleaned text starts with "Python" and ends with "!"
11. Print a final summary using conditionals:
    - If length > 30 AND contains "programming" → "📚 Technical Text"
    - If length > 30 AND NOT "programming"      → "📝 General Text"
    - If length <= 30                            → "💬 Short Text"
"""

text = "Python is an AMAZING programming lnaguage! "

# 1. Clean the text
clean_text = text.strip()

# 2. First and last CHARACTER
first_character = clean_text[0]
last_character = clean_text[-1]

# 3. First and last WORD
words = clean_text.split()
first_word = words[0]
last_word = words[-1]

# 4. Count letter "a" (case-insensitive)
count_a = clean_text.lower().count("a")

# 5. Check if theext contain "AMAZING"
contain_amazing = "AMAZING" in clean_text

# 6. Replace "AMAZING" with "awesome"
replace_text = clean_text.replace("AMAZING", "awesome")

# 7. Convert to title case
title_text = clean_text.title()

# 8. Check beginning and ending
starts_with_python = clean_text.startswith("Python")
ends_with_exclamation = clean_text.endswith("!")

