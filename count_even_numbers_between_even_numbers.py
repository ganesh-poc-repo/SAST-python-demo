n=int(input())
l=list(map(int,input().split()))
s=0
for i in range(0,n):
    if i<n-2:
        if l[i]%2==0 and l[i+2]%2==0 and l[i+1]%2==0:
            s+=1
        else:
            continue
    else:
        break
print(s)
        