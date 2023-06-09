n=int(input())
l=[]
n1=0
n2=1
for i in range(n):
    n3=n1+n2
    l.append(n3)
    n1=n2
    n2=n3
if n in l:
    print("True")
else:
    print("False")

    