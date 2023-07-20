n=int(input())
l=list(map(int,input().split()))
s=0
t=n
for i in range(0,n):
    t-=1
    s+=l[i]*(2**t)
print(s)