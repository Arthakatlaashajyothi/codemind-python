n=int(input())
for i in range(n):
    t=int(input())
    l=[]
    while t:
        r=t%10
        l.append(r)
        t=t//10
    l.sort()
    c=0
    for i in range(0,len(l)-1):
        if l[i]+1==l[i+1]:
            c+=1
    if len(l)==c+1:
        print("YES")
    else:
        print("NO")