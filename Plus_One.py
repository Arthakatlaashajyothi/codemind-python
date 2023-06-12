n=int(input())
li=list(map(int,input().split()))
s=[str(integer)for integer in li]
string=''.join(s)
res=int(string)
m=res+1
l=[]
while m:
    r=m%10
    l.append(r)
    m=m//10
l.reverse()
print(*l)