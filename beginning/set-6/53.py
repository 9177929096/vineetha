e=int(input())
count=0
sum=0
while e>0:
    rem=e%10
    sum=sum+rem
    e=e//10
print(sum)
