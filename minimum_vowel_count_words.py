def count(n):
    p='aeiou'
    c=0
    for i in n:
        if i in p:
            c=c+1
    return c
l=input().lower().split()
li=list(l)
k=[]
for i in li:
    k.append(count(i))
t=min(k)
for i in k:
    print(k.count(i))
    break
    

