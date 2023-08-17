# Approach 1 using loop
# mylist=[1,2,3,4,5]
# ele=100
# flag=0
#
# for i in mylist:
#     if i==ele:
#         print("Element found")
#         flag=1
#         break
# if flag==0:
#     print("Element not found")

# Approach 2 using in operator
mylist=[1,6,3,4,5,]
ele= 122

if ele in mylist:
    print("Element found")
else:
    print("Not found")