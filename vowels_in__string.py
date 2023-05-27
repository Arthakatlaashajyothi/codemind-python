s=input()
vowel='aeiouAEIOU'
l=[]
for i in s:
    if i in vowel and i not in l:
        l.append(i)
print(*l)