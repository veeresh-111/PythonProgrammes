import re

str1="welcome@@2To%%Python**Programming@||^%%@$"
str2="welcome to python programme"

regex=re.compile('[@_!#$%^&*()<>?/\|}{~:]')
if(regex.search(str2) == None):
    print("No special characters present in a string")
else:
    print("String contains special characters")