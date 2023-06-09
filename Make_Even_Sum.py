n=int(input())
li=list(map(int,input().split()))
p=sum(li)
if p%2==0:
    print("1")
else:
    print("0")