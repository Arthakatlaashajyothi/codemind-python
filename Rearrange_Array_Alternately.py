n=int(input())
for i in range(n):
    t=int(input())
    l=list(map(int,input().split()))
    l.sort(reverse=True)
    i=0
    j=-1
    p=[]
    while i!=len(l)and j!=0 and j!=-(len(l)//2)-1:
        p.append(l[i])
        p.append(l[j])
        i=i+1
        j=j-1
    k=[]
    k.append(l[len(l)//2])
    if len(l)%2==0:
        print(*p)
    else:
        print(*((p)+k))