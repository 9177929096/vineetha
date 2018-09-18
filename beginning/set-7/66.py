y=int(input(""))
count=0
for k in range(1,y+1):
    if(y%k==0):
       count+=1
if (count==2):
    print("yes")
else:
    print("no")
