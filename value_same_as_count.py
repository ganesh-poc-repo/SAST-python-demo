n=int(input())
l=list(map(int,input().split()))
d={}
for i in l:
    if i not in d.keys():
        d[i]=1
    else:
        d[i]+=1
s=0
for i,j in d.items():
    if i==j:
        s+=1
print(s)
