#1) Program that accepts a string and count the number of vowels
str=input("Enter string")
count=0
for i in str:
   if i in ['a','e','i','o','u']:
      count +=1
print("Number of vowels in string is",count )
      
