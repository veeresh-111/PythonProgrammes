
s=input("Enter a String  ")

# print(s[:]) # abcde
# print(s[0:5]) # abcde
# print(s[0:5:1]) # abcde
# print(s[::]) # abcde

revstr=s[::-1] # reverse string
print(revstr)

if revstr==s:
    print("Palindrome")
else:
    print("Not Palindrome")