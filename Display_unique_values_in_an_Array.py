n=int(input())
l=list(map(int,input().split()))
e=[]
for i in l:
    if l.count(i)==1:
        e.append(i)
if len(e)==0:
    print(-1)
else:
    for i in e:
        print(i,end=" ")