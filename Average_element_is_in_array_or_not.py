n=int(input())
li=list(map(int,input().split()))
p=sum(li)//len(li)
if p in li:
    print("True")
else:
    print("False")