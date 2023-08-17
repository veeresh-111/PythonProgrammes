

# Approach 1 simple swap
# mylist=[23,56,70,40]
# print(mylist)
# pos1,pos2=1,3
# mylist[pos1],mylist[pos2]=mylist[pos2],mylist[pos1]
# print(mylist)

# Approach 2 using pop() function
# mylist=[23,56,70,40]
# print(mylist)
# pos1,pos2=1,3
#
# first=mylist.pop(pos1) # 56
# seccond=mylist.pop(pos2-1)
#
# mylist.insert(1,seccond)
# mylist.insert(3,first)
#
# print(mylist)

# Approach 3 using tuple
mylist=[23,56,70,40]
print(mylist)
pos1,pos2=1,3

get=(mylist[pos1],mylist[pos2])

mylist[pos2],mylist[pos1]=get

print(mylist)