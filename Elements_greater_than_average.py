n=int(input())
l=list(map(int,input().split()))
s=0
for i in l:
        s+=i
a=s//n
c=0
for i in l:
    if i>=a:
        c+=1
    else:
        continue
print(c)