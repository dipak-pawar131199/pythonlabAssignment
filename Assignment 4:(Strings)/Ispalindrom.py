#2) Program to check whether a string is a palindrome or not using recursion. 
# palindrome string is a string if we reverse the string we get same string  as like user inputed string 
# eg. madam,aba,.etc
str=input("Enter string ")
rstr=''
for i in str[-1::-1]:
    rstr=rstr+i
print(rstr)
if str==rstr:
   print(str,"is palindrom")
else:
   print(str,"not palindrom")
