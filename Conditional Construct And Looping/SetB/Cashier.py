("""
1) A cashier has currency notes of denominations 10, 50, and 100.If the amount to be
withdrawn is input through the keyboard using input() function in hundreds, find the total
number of currency notes of each denomination the cashier will have to give to the
withdrawer
""")
wamount=int(input("Enter the amount you want to withdrawn: "))
print("total 100 Rs. notes required :",wamount/100)
print("Total 50 Rs. notes required :",(wamount % 100)/50)
print("Total 10 Rs. notes required :",((wamount % 100)%50)/10)
print("Amout remaining is:",((wamount%100)%50)%10)
