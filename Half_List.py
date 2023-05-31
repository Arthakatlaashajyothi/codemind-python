n=int(input())
li=list(map(int,input().split()))
l=[]
k=[]
for i in range(0,len(li)//2):
    l.append(li[i])
for i in range(len(li)//2,len(li)):
    k.append(li[i])
k.reverse()
print(*(k+l))