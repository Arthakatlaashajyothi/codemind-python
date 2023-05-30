def palindrome(n):
    p=str(n)
    q=p[::-1]
    if q==p:
        return True
    else:
        return False
t=int(input())
k=int(input())
l=[]
v=[]
for i in range(t,k+1):
    l.append(i)
for i in l:
    if palindrome(i):
        v.append(i)
print(*v)
    
