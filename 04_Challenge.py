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


