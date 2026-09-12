"""
============================================
  LECTURE 2 - FILE 3: CONDITIONAL STATEMENTS
  Topics: if, elif, else, Nested, Ternary
  Total Questions: 
============================================

"""

# ==========================================
#  PART A: BASIC if / else 
# ==========================================

# Q1. SIMPLE if:
#     Create a variable age = 20.
#     If age is greater than or equal to 18, print "You can vote!"

age = 20

if age >= 18:
    print("You can vote.")

#-----------------------------------------------------------------------------------------

# Q2. if-else:
#     Create a variable temperature = 35.
#     If temperature > 30, p0rint "It's hot outside!"
#     Otherwise, print "The weather is nice! "
#     Then change temperature to 20 and run again.

temp = 35

if temp > 30:
    print("It's hot outside!")
else:
    print("The weather is nice!")

#-----------------------------------------------------------------------------------------

# Q3. if-elif-else:
#     Create a variable score = 75.
#     Print the grade based on these rules:
#     - 90 and above → "Grade: A "
#     - 80 to 89     → "Grade: B "
#     - 70 to 79     → "Grade: C "
#     - 60 to 69     → "Grade: D "
#     - Below 60     → "Grade: F "

marks = 80

if marks >=90:
    print("Grade: A")
elif marks >=80:
    print("Grade: B")
elif marks >=70:
    print("Grade: C")
elif marks >=60:
    print("Grade: D")
else: 
    print("Grade: F")

#-----------------------------------------------------------------------------------------

# ==========================================
#  PART B: LOGICAL OPERATORS IN CONDITIONS 
# ==========================================

# Q4. LOGICAL OPERATORS - AND:
#     A user can access the account only if:
#     - username is correct
#     - password is correct
#
#     Use the "and" operator.

username = "admin"
password = "12345"

if username == "admin" and password == "12345":
    print("Login Successful!")
else:
    print("Invaid username or password!")

#-----------------------------------------------------------------------------------------

# Q5. LOGICAL OPERATORS - OR & NOT:
#     A customer gets a discount if:
#     - they are a student OR
#     - they are a member.
#
#     Also check whether the customer is NOT banned.

student = True
member = False
banned = False

if (student or member) and not banned:
    print("Discount Applied.")
else:
    print("No discount available.")

#-----------------------------------------------------------------------------------------