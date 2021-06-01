cr=int(input("Enter current Reading: "))
pr=int(input("Enter Previous Reading:"))
chMT=input("Enter Meter Type (domestic ,D/d) and (Industrial ,I/i) ")
def ElectricityBill(cre,pre,ch):
       if ch=='D' or ch=='d':
             if cr<=199:
                 Amout=cr*1.20
                 return Amout,1.20  
             elif cr>=200 and cr<400:
                 Amout=cr*1.50
                 return Amout,1.50
             elif cr>=400 and cr<600:
                 Amout=cr*1.80
                 return Amout,1.80
               
             elif cr>=600:
                 Amout=cr*2
                 return Amout,2
       elif ch=='I' or ch=='i':
                  amount=cr*6
                  return amount ,6  
       else :
                print("Buy") 
               
                
amout,unit=ElectricityBill(cr,pr,chMT)
if amout<100 and chMT in ['D','d']:
      amout=100
      print("--------------------Electricity Bill------------------------------")
      print("------------------------------------------------------------------") 
      print("|Current Reading | Previous Reading | Charge/Unit | Total Amount |")
      print("------------------------------------------------------------------")
      print("| \t",cr,"\t |","\t",pr,"\t    |\t",unit,"\t  |","\t",amout,"\t |")      
      print("------------------------------------------------------------------")   
elif amout >400 and chMT in ['D','d']:
      amout+=(amout*15)/100
        
      print("--------------------Electricity Bill------------------------------")
      print("------------------------------------------------------------------") 
      print("|Current Reading | Previous Reading | Charge/Unit | Total Amount |")
      print("------------------------------------------------------------------")
      print("| \t",cr,"\t |","\t",pr,"\t    |\t",unit,"\t  |","\t",amout,"\t |")      
      print("------------------------------------------------------------------")   
      print("Your amount exceeds 400 ,so you paid 15 % extra charged")
else :  
      print("--------------------Electricity Bill------------------------------")
      print("------------------------------------------------------------------") 
      print("|Current Reading | Previous Reading | Charge/Unit | Total Amount |")
      print("------------------------------------------------------------------")
      print("| \t",cr,"\t |","\t",pr,"\t    |\t",unit,"\t  |","\t",amout,"\t |")      
      print("------------------------------------------------------------------")   

