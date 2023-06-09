n=int(input())
l=[]
n1=0
l.append(n1)
n2=1
l.append(n2)
for i in range(0,n-2):
    n3=n1+n2
    l.append(n3)
    n1=n2
    n2=n3
print(*l)
    