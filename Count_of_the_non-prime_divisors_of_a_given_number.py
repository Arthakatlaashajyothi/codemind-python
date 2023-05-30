N=int(input())
l=[]
k=[]
for i in range(1,N+1):
    if N%i==0:
        l.append(i)
for i in l:
    c=0
    for j in range(1,i):
        if i%j==0:
            c=c+1
    if c!=1:
        k.append(i)
print(len(k))