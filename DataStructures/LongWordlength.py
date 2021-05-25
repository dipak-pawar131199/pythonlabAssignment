#4) Program to read a list of words and return the length of longest one
n=int(input("how many words"))
l=[]
lenl=[]
x=""
for i in range(n):
   a=input("Enter world ")
   l.append(a)
   lenl .append (len(a))
max=max(lenl )
for i in l:
    if max==len(i):
         x=i
print("world have log length is in list ",l,'is',x,"heaving length",max )
