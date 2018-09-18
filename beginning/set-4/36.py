mn=input()
a=sum(c.isalpha() for c in mn)
b=sum(c.isdigit() for c in mn)
d=sum(c.isspace() for c in mn)
spsymbl=len(xy)-a-b-d
print(spsymbl)
