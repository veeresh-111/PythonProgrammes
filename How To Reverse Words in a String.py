str="welcome to python programme"

words=str.split(' ') # ['welcome', 'to', 'python', 'programme']
print(words)
#
# words=words[-1::-1] # ['programme', 'python', 'to', 'welcome']
# print(words)

oustr="".join(words)
print(oustr)