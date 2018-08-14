n1=int(input())
n2=int(input())
for i in range(n1,n2,1)
     num=i
     sum=0
     while(num>0):
           i=i%10
           sum=sum+i**3
           i=i//10
     if(num==sum):
           print(sum)
