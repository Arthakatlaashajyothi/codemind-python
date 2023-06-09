a,b=map(int,input().split())
l=[]
k=[]
for i in range(1,a+1):
    if a%i==0:
        l.append(i)
for i in range(1,b+1):
    if b%i==0:
        k.append(i)
c=set(l)
d=set(k)
p=c.intersection(d)
print(max(p))