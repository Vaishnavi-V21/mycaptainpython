up=int(input("Enter the upper limit:"))
x=[]
x1=1
x2=1
x.append(x1)
x.append(x2)
while x1+x2<=up:
    x3=x1+x2
    x.append(x3)
    x1=x2
    x2=x3
for i in range(0,len(x)):
    print(x[i])
