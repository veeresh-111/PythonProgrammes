# input: [5,10,15,20]
# output: 50

# Approach 1 using loop with range()
# mylist=[5,10,15,20]
# sum=0
#
# for i in range(0,len(mylist)):
#     sum=sum+mylist[i]
#
# print("sum of given numbers in a list:",sum)

# Approach 2 using sum() method
mylist=[5,10,15,20]
sum=sum(mylist)
print("sum of given numbers in a list:",sum)