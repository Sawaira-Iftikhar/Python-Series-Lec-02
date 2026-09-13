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

# ==========================================
#  PART C: NESTED & ADVANCED 
# ==========================================

# Q6. NESTED if:
#     Given: age = 20, has_ticket = True
#     First check if age >= 18:
#       If yes, check if has_ticket is True:
#         If yes → "Welcome to the movie! 🎬"
#         If no  → "Please buy a ticket first."
#       If age < 18:
#         → "Sorry, you're too young."

age = 20
ticket = True

if age > 18:
    if ticket == True:
        print("Welcome to the movie :) ")
    else:
        print("please buy a ticket.")
else:
    print("Sorry, you are too young.")

#-----------------------------------------------------------------------------------------

# Q7. MEMBERSHIP in conditions:
#     Given: email = "ali@gmail.com"
#     a) Check if "@" is in the email 
#     b) Check if the email ends with ".com" 
#     c) Check if the email contains "yahoo" 
#     Print "Valid email ✅" only if ALL conditions are True.

email = "ayz@gmail.com"

if "@" in email and email.endswith(".com") and "yahoo" not in email:
    print("Valid email ✅")

#------------------------------------------------------------------------------------------

"""TERNARY OPERATOR"""
"Shortcut form of if-else funciton"

# Q8. TERNARY OPERATOR (One-line if-else):
#
#     a) age = 20 → Print "Adult"  else "Minor"
#     b) score = 45 → Print "Pass"  else "Fail"
#     c) num = 7 → Print "Even"  else "Odd"
#     d) text = "" → Print "Empty"  else "Not Empty"

# check age
age = 20
print("Adult" if age >= 18 else "Minor")

# Check score
score = 45
print("Pass" if score >= 50 else "Fail")

# Check even or odd
num = 7
print("Even" if num % 2 == 0 else "Odd")
# check if text is empty
text = " "
print("Empty" if not text else "Not Empty")

#-----------------------------------------------------------------------------------------

# ==========================================
#  PART D: REAL-WORLD SCENARIOS 
# ==========================================

# Q9. MINI PROJECT — ATM Machine:
#      Create a variable: balance = 5000
#      Create a variable: action = "withdraw"  (try "deposit", "check", "invalid")
#      Create a variable: amount = 2000

"""  Explanation

     Write conditions:
     - If action is "withdraw":
         Check if amount <= balance:
           Subtract and print new balance
         Else:
           Print "Insufficient funds! ❌"
     - If action is "deposit":
         Add amount and print new balance
     - If action is "check":
         Print current balance
     - Else:
         Print "Invalid action! 🚫"
"""

balance = 5000
action = "withdraw"
amount = 2000

if action == "withdraw":
    if amount <= balance:
        balance -= amount
        print("Withdrawal successful New Balance: ",balance)
    else:
        print("Insufficient funds.")
elif action == "deposit":
    balance += amount
    print("Deposit successfl! New balance: ", balance)
