v=int(input(""))
x=1
y=1
count=0
k=0
m=" "
if(v==0):
     print(x)
elif(v<0):
     print("negative number")
else:
   while(count<v):
     if(k==0):
          print(x,end="")
     else:
          print("",end=m)
          print(x,end="")
     nexterm=x+y
     x=y
     y=nexterm
     count+=1
     k+=1
