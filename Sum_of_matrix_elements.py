r=int(input())
c=int(input())
mat=[]
for i in range(r):
    x=list(map(int,input().split()))
    mat.append(x)
l=[]
for i in mat:
    l.append(sum(i))
print(sum(l))
