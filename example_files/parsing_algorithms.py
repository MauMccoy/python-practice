#THIS FILE CONTAINS EXAMPLES OF HOW TO PARSE ALGORITHMS
#AND HOW TO USE THEM IN PYTHON

# OPEN, READ, AND SPLIT A FILE
with open("example_files/login_attempts.txt", "r") as file:
    file_text = file.read()
usernames = file_text.split('\n')
# print(usernames)

#CREATE A FUNCTION THAT COUNTS THE USERS FAILED LOGIN ATTEMPTS
def login_check(login_list, current_user):
    counter = 0
    for i in login_list:
        if i == current_user:
            counter = counter +1
    if counter >= 3:
        return "User has been locked out due to too many failed login attempts."
    else:
        return "User can login!"
    
#TEST THE FUNCTION
print(login_check(usernames, 'heidi'))