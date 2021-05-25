# Program to swap the values of two variables
#solution-> 1) using third variable
a=int(input("Enter number:"))
b=int(input("Enter number:"))
print("Before swaping : ","a=",a,'  ',"b=",b)
temp=a
a=b
b=temp
print("After swaping : ","a=",a,'  ',"b=",b)

#solution -> 2) using EOR oprator (^)
a=int(input("Enter number:"))
b=int(input("Enter number:"))
print("Before swaping : ","a=",a,'  ',"b=",b)
a=a^b
b=a^b
a=a^b
print("After swaping : ","a=",a,'  ',"b=",b)

#solution -> 3) using additon substraction
a=int(input("Enter number:"))
b=int(input("Enter number:"))
print("Before swaping : ","a=",a,'  ',"b=",b)
a=a+b
b=a-b
a=a-b
print("After swaping : ","a=",a,'  ',"b=",b)
