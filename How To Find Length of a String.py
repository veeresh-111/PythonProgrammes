# input: welcome
# output: 7

# Approach 1 using for loop
# str='welcome'
# count=0
#
# for i in str:
#     count=count+1
# print(count) # 7

# Approach 2 using while loop and slicing
# str='welcome'
# count=0
# while str[count:]: # 0:6
#     count=count+1
# print(count) # 7

# Approach 3 using built=in function len()
# str='welcome'
# print(len(str))

# Approach 4 using join and count
str='welcome'
random_str="X"
print((random_str).join(str)) # wXeXlXcXoXmXe
print((random_str).join(str).count(random_str)) # 6
print((random_str).join(str).count(random_str)+1) # 7 length of string