n=int(input())
p=str(n)
q=str(n*n)
if q.endswith(p):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")