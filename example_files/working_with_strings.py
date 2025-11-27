#THIS FILE CONTAINS EXAMPLES OF HOW TO WORK WITH STRINGS

#CONVERT AN INTEGER TO A STRING
new_string = str(123)
print(type(new_string))  # Output: <class 'str'>

#PRINT THE LENGTH OF A STRING
print(len("security"))  # Output: 8

#CONCATENATE STRINGS
print("Hello, " + "world!")  # Output: Hello, world!(using + operator)

#APPLY .upper() METHOD TO A STRING
print("security".upper())  # Output: SECURITY

#APPLY .lower() METHOD TO A STRING
print("SECURITY".lower())  # Output: security

#DISPLAY INDEX OF A STRING
print("security"[0])  # Output: 's'

#EXTRACT A SLICE OF A STRING
print("security"[1:4])  # Output: 'ecu'

#USE THE .index() STRING METHOD
print("security".index("c"))  # Output: 2

#SEARCH FOR A CHARACTER USING .index() METHOD
print("security".index("t"))  # Output: 5