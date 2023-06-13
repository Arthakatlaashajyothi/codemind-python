n=int(input())
for i in range(n):
    t=int(input())
    li=list(map(int,input().split()))
    l=[]
    for i in range(1,t+1):
        l.append(i)
    p=[]
    q=[]
    for i in li:
        for j in l:
            if j in li and j in l:
                p.append(j)
            else:
                q.append(j)
    print(*(set(q)))   