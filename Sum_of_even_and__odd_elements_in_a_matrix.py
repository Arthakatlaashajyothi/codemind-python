r,c=map(int,input().split())
mat=[]
p=[]
q=[]
w=[]
for i in range(r):
    x=list(map(int,input().split()))
    mat.append(x)
for i in mat:
    for j in i:
        p.append(j)
for i in p:
    if i%2==0:
        q.append(i)
    else:
        w.append(i)
print(sum(q),sum(w))