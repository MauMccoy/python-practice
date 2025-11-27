#FUNCTIONS

#CREATE A SIMPLE FUCTION
def simple_function():
    print("This is a simple function.")
#CALL THE FUNCTION
simple_function()

#FUNCTION WITH PARAMETERS
def greet_user(name):
    print("Hello, " + name + "!")
    return name
current_user = greet_user("Alice")
print("Current user is:", current_user)

#RETURN VALUE FROM FUNCTION
def calculate_fails(total_attempts, failed_attempts):
    fail_percentage = (failed_attempts / total_attempts)
    return fail_percentage

percentage = calculate_fails(4, 2)
if percentage >= 0.5:
    print("Account Locked")

#EXPLORE THE INPUT AND OUTPUT OF PRINT FUNCTION
print("This is a string, but", 75, "is a number.")

#EXPLORE THE INPUT AND OUTPUT OF TYPE FUNCTION
print(type("security"))
print(type(75.2))

#EXPLORE THE MAX BUILT IN FUNCTION
print(max(4, 7, 2, 8, 5))

#USE THE SORTED FUNCTION
usernames = ["alice", "bob", "charlie", "dave", "eve", "frank"]
sorted_usernames = sorted(usernames)
print("Sorted usernames:", sorted_usernames)

