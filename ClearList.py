# Approach 1 using clear() method
# mylist=[2,5,8,3,6,7]
# print("before clear list:",mylist)
# mylist.clear()
# print("Afer clear list:",mylist)

# Approach 2 using initialize list with no values

# mylist=[2,5,8,3,6,7]
# print("before clear list:",mylist)
# mylist=[]
# print("Afer clear list:",mylist)

# Approach 3 using *=0 this will remove all elements in the list
# mylist=[2,5,8,3,6,7]
# print("before clear list:",mylist)
# mylist *=0
# print("Afer clear list:",mylist)

# Approach 4 using del() method
mylist=[2,5,8,3,6,7]
print("before clear list:",mylist)

del mylist[:]
print("Afer clear list:",mylist)