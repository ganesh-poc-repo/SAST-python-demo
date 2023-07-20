n=int(input())
l=list(map(int,input().split()))
s=0
c=0
for i in range(0,n):
    if i%2==0:
        s+=l[i]
    else:
        c+=l[i]
print(abs(s-c))