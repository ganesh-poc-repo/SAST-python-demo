n=int(input())
l=list(map(int,input().split()))
se=int(input())
for i in range(0,n):
    if l[i]==se:
        print(i)
        break
else:
    print(-1)