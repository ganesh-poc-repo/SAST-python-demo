s=input()
l=s.split()
m=10
for i in range(0,len(l)):
    c=0
    for i in l[i]:
        c+=1
    if m>c:
        m=c
print(m)