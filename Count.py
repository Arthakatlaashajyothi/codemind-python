n=int(input())
li=list(map(int,input().split()))
l=0
k=0
for i in li:
    if i%2==0:
        l=l+1
    else:
        k=k+1
print(l ,k)