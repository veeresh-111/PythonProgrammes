num = 645
sum1 = 0
rem = 0

while num != 0:
    rem = num % 10
    sum1 = sum1+(rem*rem)
    num = num/10

print("Sum of sqare of given num is:",sum1)
