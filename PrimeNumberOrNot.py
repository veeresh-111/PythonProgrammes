# natural number>1
# which has only two factors 1 and itself

num=19
count=0

if num>1:
    for i in range(1,num+1):
        if num%i== 0:
            count=count+1
    if count== 2:
        print("Prime Number is :",num)
    else:
        print("Not Prime Number:",num)