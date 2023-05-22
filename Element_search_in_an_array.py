n=int(input())
li=list(map(int,input().split()))
m=int(input())
for i in range(1,n+1):
    if m not in li:
        print("False")
        break
else:
    print("True")
        
