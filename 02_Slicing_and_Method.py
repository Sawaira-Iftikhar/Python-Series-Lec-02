"""
============================================
  LECTURE 2 - FILE 2: SLICING & METHODS
  Topics: Slicing, Negative Slicing, String Methods
  Total Questions: 
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