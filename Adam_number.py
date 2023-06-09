def reverse(n):
    rev=0
    while n:
        r=n%10
        rev=rev*10+r
        n=n//10
    return rev
s=int(input())
temp=s
p=temp*temp
r=reverse(temp)
q=r*r
k=reverse(q)
if p==k:
    print("True")
else:
    print("False")