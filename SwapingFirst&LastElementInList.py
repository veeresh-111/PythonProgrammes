#
# mylist=[20,10,40,50,70]
# size=len(mylist) # 5
# print("before swaping list:",mylist)

# Approach 1
# temp=mylist[0]
# mylist[0]=mylist[size-1]
# mylist[size-1]=temp

# Approach 2
# mylist[0],mylist[-1]=mylist[-1],mylist[0]

# Approach 3 Using tuple
# get=(mylist[-1],mylist[0])
# mylist[0],mylist[-1]=get

# Approach 4 * operand
mylist=[20,10,40,50,70]
start,*middle,end=mylist
mylist=[end,*middle,start]

#Approach 5 using pop()
# mylist=[20,10,40,50,70]
#
# first=mylist.pop(0) # 20
# last=mylist.pop(-1) # 70
#
# mylist.insert(0,last)
# mylist.append(first)

print("after swaping list is:",mylist)