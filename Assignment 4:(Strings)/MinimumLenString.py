
#8) Write a function that reads multiple strings, and will return the string in which the 
#number of characters are minimum
def minimumlenstr():
   l=[] # to store n string 
   lenl=[] # empty list to store length of string you enter in l list
   k=''
   m=0
   n=int(input("how many strings?"))
   for i in range(n):
       a=input("Enter string")
       l.append(a)
       lenl.append (len(a))
   m=min(lenl) # find Minimum length of string from lenl
   for i in l:
       if m==len(i):# compare each string length from l with m
          k=i
   print("\n",k,'is minimum length string you enter')
minimumlenstr ()
