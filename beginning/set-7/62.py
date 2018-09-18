a=input()
count=0
for k in range(0,len(a)):
      if(a[k]=='0' or a[k]=='1'):
              count+=1
      if count==len(a):
           print("yes")
      else:print("no")
