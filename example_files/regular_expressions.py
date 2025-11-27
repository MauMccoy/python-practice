# Regular Expressions 
import re

#EXTRACT EMAIL ADDRESSES
email_log = """Email received June 2 from user@gmail.com, email received June 3 from user2@gmail.com, " \
+"email received June 4 from user3@gmail.com, email received June 5 from user4@gmail.com"""
print(re.findall("\w+@\w+\.\w+", email_log))

#REGULAR EXPRESSION REGEX
print(re.findall("ts", "tsnow, tshah, bmoreno"))

#SYMBOLS FOR CHARACTER TYPES
print(re.findall("\w","h32rb17"))
print(re.findall("\d","h32rb17")) #/d FINDS ALL SINGLE DIGITS
print(re.findall("\s","h 32rb 17")) #/s FINDS ALL SINGLE SPACES
print(re.findall("\.","h32.rb17")) #. FINDS SINGLE PERIODS

#SYMBOLS TO QUANTIFY OCCURRENCES
print(re.findall("\d+","h32rb17")) #+ FINDS ONE OR MORE OCCURRENCES
#THE * SYMBOL REPRESENTS ZERO, ONE, OR MORE OCCURRENCES OF A SPECIFIC CHARACTER
print(re.findall("\d*","h32rb17")) #* FINDS ZERO OR MORE OCCURRENCES
#BRACKETS INDICATE A SPECIFIC NUMBER OF OCCURRENCES
print(re.findall("\d{2}","h32rb17 k89e37 m07y56")) #{n} FINDS EXACTLY n OCCURRENCES
#{x,y} FINDS BETWEEN x AND y OCCURRENCES
print(re.findall("\d{1,3}","h32rb17 k89e37 m07y56"))        

#CONSTRUCTING PATTERNS
pattern = "\w+:\s\d+"
employee_loggins_string = """1001 bmoreno: 12 Marketing 1002 tshah: 7 Human Resources 1003 sgilmore: 5 Finance"""
print(re.findall(pattern, employee_loggins_string))