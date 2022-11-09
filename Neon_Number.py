N=int(input())
tem=N
p=N*N
sum=0
while p!=0:
    r=p%10
    sum=sum+r
    p=p//10
if tem==sum:
    print("Neon Number")
else:
    print("Not Neon Number")
    
    
    