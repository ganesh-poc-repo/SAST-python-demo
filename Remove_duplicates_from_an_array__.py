n=int(input())
l=list(map(int,input().split()))
s=list(set(l))
for i in s:
    print(i,end=" ")