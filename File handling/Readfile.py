# open abc.txt in write mode

f1=open('abc.txt','w')
f1.write(input("enter contents into file"))
f1.close()

# following code to read content from abc.txt

f=open('abc.txt','r')
a=f.readline()
print(a)

f.close()
