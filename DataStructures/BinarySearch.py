#2) Program to search for an element in a list using binary search operation
def binsearch (lb,ub,ele,l):
   if lb<=ub:
     mid=(lb+ub)//2
     if l[mid]==ele:
        return mid
     elif l[mid]>ele:
           return  binsearch (lb,mid-1,ele,l)
     else :
           return binsearch (mid+1,ub,ele,l)
   else:
        return -1
l=[1,4,8,11,15,17,25]
print("ernter elemet to search",end=" ")
ele=int(input())
pos=binsearch(0,len(l)-1,ele,l)
if pos !=-1:
   print (ele,"is found at position",pos)
else:
   print (ele,"not found")
