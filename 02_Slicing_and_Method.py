"""
============================================
  LECTURE 2 - FILE 2: SLICING & METHODS
  Topics: Slicing, Negative Slicing, String Methods
  Total Questions: 6
============================================

"""

# ==========================================
#  PART A: SLICING 
# ==========================================

# Q1. Given: text = "ABCDEFGHIJ"
#     Extract and print the following using slicing [start:stop]:
#     a) First 3 characters
#     b) Characters from index 2 to 6
#     c) Last 4 characters (using positive indices)
#     d) Everything from index 5 to the end
#     e) The entire string using slicing

name = "Ahtsham"
# first 3 characters
print("first 3: ",name[0:3])
#Character form index 2 to 6
print("2 to 6: ", name[2:7])
# last 4 characters using positive indices
print("last 4: ",name[6:7])
# Everything from index 5 to te end
print("5 to end: ",name[5:len(name)])
# Te entire string using slicing
print("full: ",name[0:7])

#----------------------------------------------------------------------------------------

# Q2. REVERSE A STRING using slicing:
#     Given: word = "PYTHON"
#     a) Reverse the entire string
#     b) Reverse only the first half
#     c) Reverse only the second half

word = "PYTHON"

# Reverse the entire string
print("Full reverse:", word[::-1])
# Reverse only the first half
print("First half reversed:", word[:3][::-1] + word[3:])
# Reverse only the second half
print("Second half reversed:", word[:3] + word[3:][::-1])

#----------------------------------------------------------------------------------------

# ==========================================
#  PART B: NEGATIVE SLICING 
# ==========================================

# Q3. Given: letter = "Hello World"
#     Use NEGATIVE indices to extract:
#     a) Last 5 characters
#     b) Everything except the last 6 characters
#     c) Characters from -8 to -3
#     d) The word "World" using only negative indices

letter = "Hello World"
# Last 5 letters
print("Last 5: ",letter[-5: ])
# all other letters except the last 6
print("Except last 6: ",letter[:-6])
# print -8 to -3 letters
print("-8 to -3",letter[-8 :-3])
# world letter using only negative indeces
print('"world" negative: ',letter[-5:])

#----------------------------------------------------------------------------------------

# ==========================================
#  PART C: STRING METHODS (Q6 - Q10)
# ==========================================

# Q4. CASE METHODS:
#     Give the variable name or any sentence then use these methods 
#     Print the result of each:
#     a) .upper()
#     b) .lower()
#     c) .title()
#     d) .capitalize()
#     e) .swapcase()

msg = "WoRkinG on PythON SeRieS"
# Converting into upercase
print("Upper Case: ", msg.upper())
# Converting into lowercase
print("lower Case: ",msg.lower())
# Converting into Titlecase that capitalize each first word
print("Title Case: ",msg.title())
# Converting only the first character of string into Capitalcase
print("Capitalize Case: ",msg.capitalize())
#Swap uppercase letter into lowercase and lowercase to uppercase
print("swap Case: ",msg.swapcase())

#----------------------------------------------------------------------------------------

# Q5. SEARCH & REPLACE METHODS:
#     Given: sentence = "I love Python and Python loves me"
#     a) Count how many times "Python" 
#     b) Find the index of first "Python" 
#     c) Find the index of "Java" 
#     d) Replace "Python" with "JavaScript" 
#     e) Replace only the FIRST "Python" 

sentence = "I love Python and Python loves me"
# Count how many "Python" words are present in sentence
print("Count of 'Python': ",sentence.count("Python"))
# Find the index of the first "Python"
print("first 'Python': ",sentence.find("Python"))
# Find the index of java
print("'Java' at: ",sentence.find("Java"))
# Replace all "Python" with "javascript"
print('Replace all process: ',sentence.replace("Python", "JavaScript"))
# Replace only the Frist "Python"
print("Replaced firstc process: ",sentence.replace("Python","JavaScript",1))

#----------------------------------------------------------------------------------------

# Q6. STRIP & SPLIT METHODS:
#     a) Given: messy = "   Hello World   "
#        Remove leading/trailing spaces 
#        Remove only leading 
#        Remove only trailing
#     b) Given: csv_data = "apple,banana,cherry,date"
#        Split into a list 
#     c) Given: words = ["Python", "is", "awesome"]
#        Join into a string 

messy = "   Hello World   "

# Strip Methods
print('Stripped: ','"' + messy.strip() + '"')
print('Left-Stripped: ','"' + messy.lstrip() + '"')
print('Right-Stripped: ','"' + messy.rstrip() + '"')

# Split the CSV data into a list 
csv_data = "apple,banana,cherry,date"

print("Split: ",csv_data.split(","))

# Join words into a String (convert list into string)

words = ["Python", "is", "awesome"]

print("Joined: "," ".join(words))

#----------------------------------------------------------------------------------------


