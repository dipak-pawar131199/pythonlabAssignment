#Python program to count the number of even and odd numbers from a series of numbers 5 to 100.
e=0;o=0
for i in range(5,101):
         if i % 2==0:
             e=e+1
         else:
              o=o+1
print("how many even number in 5 to 100 is:",e)
print("how many odd number in 5 to 100 is:",e)

