
#8) Write a function that reads multiple strings, and will return the string in which the 
#number of characters are minimum
def minimumlenstr():
   l=[]
   lenl=[]
   k=''
   m=0
   n=int(input("how many strings?"))
   for i in range(n):
       a=input("Enter string")
       l.append(a)
       lenl.append (len(a))
   m=min(lenl)
   for i in l:
       if m==len(i):
          k=i
   print("\n",k,'is minimum length string you enter')
minimumlenstr ()
