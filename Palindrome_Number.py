def palindrome(n):
    r=str(n)
    p=r[::-1]
    if r==p:
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
    