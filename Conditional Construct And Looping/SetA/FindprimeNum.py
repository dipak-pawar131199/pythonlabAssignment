# Program to display all prime numbers within an interval
# Defination :Prime number is a number whitch is divisible by one or itself
# eg. num=3 which is divisible by 3 and 1 only

def prime(num):
               i=2;flag=False
               while i<=num/2:
                      if  num%i==0:
                            flag=True
                            break
                      i+=1
               if flag== False:
                    print("Prime number's are:", num)                  
               
end=int(input("Enter last number of interval:"))
i=1
while i<=end:
            x=prime(i)
            i=i+1
          
         
   

