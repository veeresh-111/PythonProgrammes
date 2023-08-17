# 5!--> 1*2*3*4*5 = 120

# Approach 1
# fact=1
# num=5
#
# if num<0:
#     print("Factorial does not exist for nagative number:")
# elif num==0:
#     print("The Factorial of 0 is 1")
# else:
#     for i in range(1,num+1):
#         fact=fact*i
#     print("The factorial of", num, "is", fact)

# approach 2
def factorial(n):
    # if(n==0 or n==1):
    #     return 1
    # else:
    #     return n*factorial(n-1)

    # ternary operator means in single line
    return 1 if(n==0 or n==1) else n*factorial(n-1)

num=5
print("The factorial of", num, "is", factorial(num))