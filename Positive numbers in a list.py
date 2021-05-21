l1=[12,-7,5,64,-14]
l2=[12,14,-95,3]
for i in l1:
    if i>0:
        print(i,end=' ',sep=' ')
a=[i for i in l2 if i>=0]
print (a)
