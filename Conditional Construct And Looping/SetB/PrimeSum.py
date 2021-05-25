#3) Find the sum of all the primes below 100.
def Sumprime(num):
     
      i=2;flag=False
      while i<=num/2:
                if num % i==0:
                  flag=True
                  break
                i=i+1
      if  flag==False:
           return num
      else:
           return 0      
i=int (input("Enter a number below you want to calculate sum of prime number's:"))
sum=x=0
while i>=1:
         x=Sumprime(i)
         sum=sum+x 
         i=i-1
print(sum-1)

