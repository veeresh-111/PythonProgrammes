
# Approach 1 using slicing method
# mylist=[1,2,3,4,5,6]
# print("before copy list:",mylist)
# mylist_copy=mylist[:]
# print("After copy list:",mylist_copy)

# Approach 2 using extend() method
# mylist=[1,2,3,4,5,6]
# print("before copy list:",mylist)
# mylist_copy=[]
# mylist_copy.extend(mylist)
# print("After copy list:",mylist_copy)

# Aproach 3 using list() method
# mylist=[1,2,3,4,5,6]
# print("before copy list:",mylist)
# mylist_copy=list(mylist)
# print("After copy list:",mylist_copy)

# Aproach 4 using copy() method
# mylist=[1,2,3,4,5,6]
# print("before copy list:",mylist)
# mylist_copy=mylist.copy()
# print("After copy list:",mylist_copy)

# Aproach 5 using list comprehension
mylist=[1,2,3,4,5,6]
print("before copy list:",mylist)
mylist_copy=[i for i in mylist]
print("After copy list:",mylist_copy)