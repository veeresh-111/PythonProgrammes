# mylist=[10,100,40,2,25,70]
# output:
# smallest is 2
# largest is 100

# Approach 1 using sort() then find smallest and largets number in list
# mylist=[10,100,40,2,25,70]
# mylist.sort()
# print(mylist) # [2,10,25,40,70]
#
# print("Smallest number in a list:",mylist[0])
# print("Largest number in a list:",mylist[-1])

# Approach 2 using max() and min() built-in method

mylist=[10,100,40,2,25,70]

print("Smallest number in a list:",min(mylist))
print("Largest number in a list:",max(mylist))