n=int(input())
m=int(input())
l=[]
for i in range(1,n):
    if n%i==0:
        l.append(i)
p=sum(l)
if p==m:
    print("Amicable")
else:
    print("Not Amicable")
    