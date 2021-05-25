# 3) Program to find the factors of a number x.
num=int(input())
print("Factors of number is : ")
i=1
while i<=num:
         if num % i==0:
             print(i)
         i=i+1
