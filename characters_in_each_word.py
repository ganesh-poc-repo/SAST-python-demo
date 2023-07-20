s=input()
l=s.split()
for i in range(0,len(l)):
    c=0
    for i in l[i]:
        c+=1
    print(c,end=" ")