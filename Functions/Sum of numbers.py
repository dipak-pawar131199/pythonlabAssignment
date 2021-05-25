("""
 4) Write a recursive function for calculating sum of numbers up to n, where sum can be
shown as;
Sum = 0+1+2+3+........+n
""")
num =int(input("Enter number up to you want to calculate Sum of N numbers: "))
def calSum(num):
        sum=0
        while num>0:
                sum+=num
                calSum(num-1) # recursive call to function calSum()
                num=num-1
        return sum
result=calSum(num)
print("Sum of series 0+1+2+3+......+",num,"is : ",result)
