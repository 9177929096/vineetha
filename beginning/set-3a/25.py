b=int(input(""))
lst=[int(z) for z in input().split()]
a=0
for i in range(0,b):
     a+=lst[i]
print(int(a/b))
