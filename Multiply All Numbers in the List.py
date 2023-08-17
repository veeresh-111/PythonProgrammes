# input: [2,3,4]
# output: 24 2*3*4=24

# Approach 1 using traversal
# mylist=[2,3,4,]
# mul=1
#
# for x in mylist:
#     mul=mul* x
#
# print("multiply of given numbers in a list:",mul)

# Approach 2 using numpy.prod() * install numpy package
import numpy
mylist=[2,3,4]
mul=numpy.prod(mylist)
print("multiply of given numbers in a list:",mul)