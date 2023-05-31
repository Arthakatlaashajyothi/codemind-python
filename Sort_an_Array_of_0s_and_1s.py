n=int(input())
li=list(map(int,input().split()))
l=[]
m=[]
c=0
for i in li:
    if i==0:
        l.append(i)
for j in li:
    if j==1:
        m.append(j)
print(*(l+m))