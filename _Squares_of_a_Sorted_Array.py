n=int(input())
li=list(map(int,input().split()))
q=[]
for i in li:
    p=i*i
    q.append(p)
q.sort()
print(*q)
    