r,c=map(int,input().split())
mat=[]
w=[]
p=[]
q=[]
h=[]
for i in range(r):
    x=list(map(int,input().split()))
    mat.append(x)
for i in range(0,len(mat),2):
    w.append(mat[i])
for i in range(1,len(mat),2):
    p.append(mat[i])
for i in p:
    h.append(sum(i))
for i in w:
    q.append(sum(i))
print(sum(q),sum(h))