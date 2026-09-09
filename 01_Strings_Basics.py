"""
============================================
  LECTURE 2 - FILE 1: STRINGS BASICS
  Topics: Strings, Escape Sequences, Indexing
  Total Questions: 
============================================

"""
# ==========================================
#  PART A: CREATING STRINGS 
# ==========================================

# Q1. Create three string variables using:
#     a) Single quotes
#     b) Double quotes
#     c) Triple quotes (multi-line)
#     Print all three.

string1 = "My name is Sawaira."
string2 = 'I am university Student.'
string3 = """what!
           do you mean i got the
           chance """

print("Double quotes: ", string1)
print("Single quotes: ", string2)
print("Triple quotes: ", string3)

#------------------------------------------------------------------------------

# Q2. What happens if you try to put a single quote inside a
#     single-quoted string? Try it and fix it TWO different ways.
#
#     Broken:  msg = 'It's a beautiful day'
#     Fix 1:   
#     Fix 2:  

print("first way:")
print("It's a beautiful day.")
print("second way:")
print('It"s a beautiful day.')

#------------------------------------------------------------------------------


# Q3. String Concatenation & Repetition:
#     a) Create first_name = "Python" and last_name = "Developer"
#        Concatenate them with a space in between.
#     b) Create a string "Ha" and repeat it 5 times using *.
#     c) What happens if you try "Hello" * 2.5? Try it and
#        write the error as a comment.

"(a):  String Concatenation "

first_name = "Sawaira"
last_name = "Iftikhar"
full_name = first_name + " "+last_name
print("full_name:",full_name)

"(b):  String Repetition "

laugh = "Ha" * 5
print("laugh: ",laugh)

"(c):"
"If i try 'hello' * 5 then it will show error bcz string store non-int value."

#------------------------------------------------------------------------------

# ==========================================
#  PART B: ESCAPE SEQUENCES 
# ==========================================

# Q4. Use escape sequences to print EXACTLY this output:
#
#     He said, "Hello!"
#     Then he walked away.
#     Path: C:\Users\name\Documents
#
#     (You must use \", \n, and \\ at minimum)

print("He said, \"Hello!\"\nThen he walked away.\nPath: C:\\Users\\name\\Documents")

#------------------------------------------------------------------------------

# Q5. What is a RAW string? Create a raw string that contains
#     \n and \t but prints them LITERALLY (not as new line/tab).
#     Compare it with a normal string.

# Normal string
normal = "Hello\nWorld"

# Raw string
raw = r"Hello\nWorld"

print("Normal:", normal)
print("Raw:", raw)

#------------------------------------------------------------------------------

# ==========================================
#  PART C: INDEXING 
# ==========================================

# Q6. Given the string text = "PYTHON", use POSITIVE indexing
#     to print each character one by one.

name = "SAWAIRA"

print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])
print(name[6])
