n=int(input())
l=list(map(int,input().split()))
j=0
for k in range(0,n):
    c=0
    for i in l:
        if l[j]>i:
            c+=1
    print(c,end=" ")
    j+=1