xy=int(input())
if(xy<=1000):
    storage=input()
    storage=[int(b) for b in storage.split()]
    zz=sorted(storage[0:xy])
for i in range(0,xy):
     if(i<xy-1):
           g=' '
     else:
         g=''
     print(zz[i],end=g)
