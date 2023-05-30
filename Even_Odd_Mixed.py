n=int(input())
l=[]
while n:
    r=n%10
    l.append(r)
    n=n//10
k=[]
o=[]
for i in l:
    if i%2==0:
        k.append(i)
    else:
        o.append(i)
if len(k)==len(l):
    print("Even")
elif len(o)==len(l):
    print("Odd")
else:
    print("Mixed")