s=input().lower()
c=0
k=0
m=0
l=0
for i in s:
    if i.isalpha():
        k+=1
    elif i.isdigit():
        l+=1
    elif i==" ":
        m+=1
    else:
        c=c+1
print(c)