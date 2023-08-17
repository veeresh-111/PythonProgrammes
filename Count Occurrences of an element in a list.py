# mylist=[10,30,50,10,70,60,10]
# x=10
# output=3
# 10 appear in the list is 3 times

# Approach 1 using loop
# mylist=[10,30,50,10,70,60,10,50]
# x=50
# count=0
#
# for ele in mylist:
#     if ele==x:
#         count=count+1
#
# print("{} has occured {} times".format(x,count))

# Approach 2 using count() method
# mylist=[10,30,50,10,70,60,10,50]
# x=10
# print("{} has occured {} times".format(x,mylist.count(x)))

# Approach 3 using counter() method
from collections import Counter
mylist=[10,30,50,10,70,60,10,50]
x=60
dic=Counter(mylist) # {10:3, 30:1, 50:2, 70:1, 60:1}
print("{} has occured {} times".format(x,dic[x]))