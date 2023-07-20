n=int(input())
l=list(map(int,input().split()))
d={}
for i in l:
    if i not in d.keys():
        d[i]=1
    else:
        d[i]+=1
a=[]
for i,j in d.items():
    if i==j:
        a.append(i)
s=0
if len(a)==0:
    print(-1)
else:
    for i in a:
        s+=i
    a=s/len(a)
    print('%.2f'%a)