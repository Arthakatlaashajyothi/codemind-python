n=int(input())
l=[]
for i in range(1,n):
    if n%i==0:
        l.append(i)
p=sum(l)
if n<p:
    print("True")
else:
    print("False")
    