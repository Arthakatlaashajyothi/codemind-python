n=list(map(int,input().split()))
m=list(map(int,input().split()))
i=0
j=0
l=[]
p=0
q=0
while i!=len(n) and j!=len(m):
    if n[i]>m[i]:
        p=p+1
    if n[i]<m[i]:
        q=q+1
    i=i+1
    j=j+1
print(p,q)