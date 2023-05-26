n=input().lower()
p=list(n)
d={}
for i in p:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
for i in d:
    if d[i]!=1:
        print("False")
        break
else:
    print("True")