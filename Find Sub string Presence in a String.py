# if sub-string found in the given string find() returns position of sub-string
# if sub-string is not found in the given string find() returns -1

str="welcome to python programme"
sub_str='python'

print(str.find(sub_str)) # 11

if(str.find(sub_str))== -1:
    print("Not found")
else:
    print("Found")