("""
1) Write a function that performs the sum of every element in the given number unless it
comes to be a single digit.
Example 12345 = 6
""")

def Calsum(num):
        c=0;sum=0
        while num>0: # loop for calcuating sum of digits of a number
                 lastdigit=num%10
                 sum+=lastdigit
                 num=num//10
        k=sum
        while k>0:# loop for count number of digit of sum
               c=c+1
               k=k//10        
        if c>1: # if digit count 'c' >1
            Calsum(sum) # recursive call to Calsum() function
        else:
            print(sum) # display sum whose digit count is 1
num=int(input("Enter number: "))
Calsum(num)

