n=int(input())
l=[]
while n:
    p=n%10
    l.append(p)
    n=n//10
c=0
for i in l:
    if l.count(i)==1:
        c+=1
if c==len(l):
    print("Unique Number")
else:
    print("Not Unique Number")