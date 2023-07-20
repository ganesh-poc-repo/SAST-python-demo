n=int(input())
l=list(map(int,input().split()))
if n==1:
    print(l[-1])
elif n==2:
    print(max(l))
else:
    s=list(set(l))
    s.sort()
    print(s[-3])