#2) Write a program in Python, A library charges a fine for every book returned late. For first
#5 days the fine is 50 paisa, for 6-10 days fine is one rupee and above 10 days fine is 5
#rupees. If you return the book after 30 days your membership will be cancelled. Write a
#program to accept the number of days the member is late to return the book and display
#the fine or the appropriate message.
ndays=int(input("Enter how days late you return book to library:"))
if ndays<=5:
     print("you return book",ndays,' day late')
     print("So, you have to give fine for late submit book is:",50,'paisa')
elif ndays>=6 and ndays <=10:
     print("you return book",ndays,' days late')
     print("So, you have to give fine for late submit book is:",1,'Rs.')
elif ndays>10 and ndays<=30:
     print("you return book",ndays,' days late')
     print("So, you have to give fine for late submit book is:",5,'Rs.')
elif ndays>30:
     print("You loss our membership!!!....")
     



