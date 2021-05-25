# armstrong num is a number sum of digit power =digit
# eg. 1634=(1^4)+(6^4)+(3^4)+(4^4)=1634
num=int(input("Enter number to check is armstrong: "))
k=num
l=num
#find how many digit number user enter
c=0
while k>0:
    c=c+1
    k=k//10
sum=0
while num>0:
      lastdigit=num%10
      sum +=(lastdigit**c)
      num=num//10
if sum==l:
    print(l,"is armstrong")
else:
   print("not")
