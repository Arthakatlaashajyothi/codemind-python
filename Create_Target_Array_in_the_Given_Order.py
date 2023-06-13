n=int(input())
li=list(map(int,input().split()))
m=int(input())
k=list(map(int,input().split()))
m=[]
i=0
j=0
while i!=len(li) and j!=len(li):
    m.insert(k[j],li[i])
    i=i+1
    j=j+1
print(*m)