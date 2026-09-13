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

if rules_passed== 5:
    print("Verdict: Strong Password!")
elif rules_passed >= 3:
    print("Verdict: Medium Passwrod")
elif rules_passed >= 1:
    print("Verdict: Weak Password")
else:
    print("Verdict: Very WEak Password")

print("==============================================")

