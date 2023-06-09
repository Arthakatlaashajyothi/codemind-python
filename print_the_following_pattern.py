n=int(input())
l=[]
for i in range(1,n+1):
    l.append(i)
s=[str(integer) for integer in l]
string=''.join(s)
n=int(string)
p=str(n)
k=len(p)
while n:
    a=n%10**k
    print(a)
    n=n//10
    