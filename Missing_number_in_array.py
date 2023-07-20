t=int(input())
for i in range(0,t):
    n=int(input())
    l=list(map(int,input().split()))
    for j in range(1,n+1):
        if j in l:
            continue
        else:
            print(j)