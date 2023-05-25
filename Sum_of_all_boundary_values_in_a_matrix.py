c,r=map(int,input().split())
mat=[]
p=[]
k=[]
h=[]
for i in range(r):
    x=list(map(int,input().split()))
    mat.append(x)
for i in range(0,len(mat),len(mat)-1):
    p.append(mat[i])
for i in range(1,len(mat)-1,1):
    k.append(mat[i])
for i in k:
    for j in range(0,len(i),len(i)-1):
        h.append(i[j])
a=[]
for i in p:
    for j in i:
        a.append(j)
print(sum(h)+sum(a))