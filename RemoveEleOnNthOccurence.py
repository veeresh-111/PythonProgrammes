
mylist=["india","for","india","for","india","india"]
word='india'
n=3

count=0
for i in range(0,len(mylist)-1):
    if mylist[i]== word:
        count=count+1
        if count==n:
            del mylist[i]

print("Updated list is:",mylist)