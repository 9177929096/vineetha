rs,b=input().split()
rs,b=int(rs),int(b)
list=[int(c) for c in input().split()]
count=0
for i in range(0,rs):
      if b==list[i]:
           print("yes")
           break
      else:print("no")
