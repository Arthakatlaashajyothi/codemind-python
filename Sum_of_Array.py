n=int(input())
li=list(map(int,input().split()))
q=[]
p=[]
for i in li:
    if i%2==0:
        q.append(i)
    else:
        p.append(i)
print(sum(q)+sum(p))