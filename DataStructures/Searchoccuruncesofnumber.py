#3) Program to search the number of times a particular number occurs in a lists
def search (ele):
   """function to find occurence of element in list"""
   count=0
   for i in l:
      if i==ele:
         count=count+1
   print(ele," found in",l,'is ',count,'times')     
l=[]
n=int(input("how many elements you wnat to store in list?\n"))
for i in range(n):
    l.append(int(input("enter ele in list ")))
print(l)
print("Enter element to search occurence of ele in list ",end=' ')
ele=int(input())
search(ele)
