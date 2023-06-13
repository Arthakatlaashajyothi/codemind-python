n=int(input())
li=list(map(int,input().split()))
for i in li:
    if li.count(i)>n//2 and li.count(i)!=1:
        print(i)
        break
        