#7) Program to match a string that contains only upper and lowercase letters, numbers, and 
#underscores. (Accept a string from the user and pass string as a parameter for the user￾defined function).
import re
def mymatch(str):
   r=re.findall(r"\b[a-zA-Z0-9_]+\b",str)
   print("match string for pattern")
   for i  in r:
      print(i)
        
   
str=input("Enter string")
print(str)
mymatch(str)
