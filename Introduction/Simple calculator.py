# Program to make simple calculator
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
ch=input(" Enter for opration symbol addition (+),substraction (-),substraction (*),substraction (/), % (get remainder) and for exit enter '$' ")

if ch=='+':
            print("Sum is : ",num1+num2)
                
if ch== "-":
                print("Difference is : ",num1-num2) 
if ch=='*':
                print("Multiplication is : ",num1*num2) 
if ch=='/':
                print("Division is : ",num1-num2) 
if ch=='%':
               print("Moduls is : ",num1%num2) 
if ch=='$':
      print("Buy");
                

