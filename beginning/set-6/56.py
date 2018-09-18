rs=input()
count=0
count1=0
for k in range(0,len(rs)):
    if((rs[k]>='a') and (rs[k]<='z') or (rs[k]>'A') and (rs[k]<'Z')):
            count=1
    elif((rs[k]=='1') or (rs[k]=='2') or (rs[k]=='3') or (rs[k]=='4') or (rs[k]=='5') or (rs[k]=='6') or (rs[k]=='7') or (rs[k]=='8') or (rs[k]=='9') or (rs[k]=='0')):
            count1=1
if count+count1==2:
     print("yes")
else:print("no")
