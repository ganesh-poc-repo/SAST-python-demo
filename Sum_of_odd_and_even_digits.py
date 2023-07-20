n=int(input())
l=list(map(int,input().split()))
c=0
s=0
for i in range(0,n):
    if i==0 or i%2==0:
        c+=l[i]
    else:
        s+=l[i]
if c-s==0:
    print('YES')
else:
    print('NO')