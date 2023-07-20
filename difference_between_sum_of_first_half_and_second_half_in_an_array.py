n=int(input())
l=list(map(int,input().split()))
h=int(n/2)
s=0
for i in range(0,h):
    s+=l[i]
c=0
for j in range(h,n):
    c+=l[j]
print(abs(s-c))