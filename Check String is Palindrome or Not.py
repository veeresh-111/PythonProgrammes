1. Using a Loop
def reverse_string_loop(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str
user_input = input("Enter a string to reverse: ")
reversed_string = reverse_string_loop(user_input)
print("Reversed string:", reversed_string)
if reversed_str==s
   print("given string is palendrome")
else
   print("given string is not palendrome")

2. using slicing method
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

3. Using reversed() and join()
python
Copy code
def reverse_string_reversed(s):
    return ''.join(reversed(s))

user_input = input("Enter a string to reverse: ")
reversed_string = reverse_string_reversed(user_input)
print("Reversed string:", reversed_string)
if reversed_str==s
   print("given string is palendrome")
else
   print("given string is not palendrome")
