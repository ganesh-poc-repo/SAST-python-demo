n=int(input())
a=list(map(int,input().split()))
d={}
for i in a:
    if i not in d.keys():
        d[i]=1
    else:
        d[i]+=1
for i in d.keys():
    print(i,d[i],end=" ")
