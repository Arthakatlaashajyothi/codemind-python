X,Y=map(int,input().split())
if X%2==0 and (Y%2==0 or X>0):
    print("YES")
else:
    print("NO")