def palindrome(n):
    p=str(n)
    r=p[::-1]
    if p==r:
        return True
    else:
        return False
t=int(input())
for i in range(t):
    m=int(input())
    if palindrome(m):
        print("True")
    else:
        print("False")