rs,a=input().split()
rs,a=int(rs),int(a)
list=[int(k) for k in input().split()]
count=0
for i in range(0,rs):
      if a==list[i]:
        count+=1
print(count)
