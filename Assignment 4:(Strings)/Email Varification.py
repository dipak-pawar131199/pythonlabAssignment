#5) Program to accept an email address from the user and validate using regular expression
import re
str=input("Enter email to varified")
r=re.search(r'[\D\w.]\w+[@]\w+',str)
if r:
  print("Valid email")
else:
  print("Invalid email")
