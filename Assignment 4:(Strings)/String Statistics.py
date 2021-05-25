#3) Program that reads a line and prints its statistics like: 
#Number of uppercase letters: 
#Number of lowercase letters: 
#Number of alphabets: 
#Number of digits
import sys # to execute exit() import sys module
print("\n------with predefine functions-------")
str=input("enter string\n")
al=up=lc=di=0
for i in str:
  if i.isalpha():
    al+=1
    if i.isupper():
       up+=1
    else:
       lc=lc+1
  elif i.isdigit():
       di+=1
  else:
       print("invalid input")
       exit()
print("Number of alphabets in str",al)
print("Number of uppercase laters in string",up)
print("Number of lowercase laters in string",lc)
print("Number of digit in string",di)
