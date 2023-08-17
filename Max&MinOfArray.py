

arr=[30,20,50,40,10]


# finding max value in array
max=arr[0]
n=len(arr)

for i in range(1,n):
    if arr[i]>max:
        max=arr[i]

print("Maximum element is:",max)


# finding mon of array
min=arr[0]
n=len(arr)

for i in range(1,n):
    if arr[i]<min:
        min=arr[i]

print("Minimum element is:",min)