
# Approach using simple method
# mylist=[2,45,6,30,80]
# mylist.sort()
# print(mylist)
#
# print("First largest number in list:",mylist[-1])
# print("Second latgest number in the list:",mylist[-2])


# Approach 2 using set and remove , max methods

mylist=[2,45,6,30,80]
new_mylist=set (mylist)
print(new_mylist)

new_mylist.remove(max(new_mylist))
print(new_mylist)

print(max(new_mylist))


