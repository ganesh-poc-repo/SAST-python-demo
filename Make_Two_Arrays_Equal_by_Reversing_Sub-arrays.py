a=int(input())
l1=list(map(int,input().split()))
b=int(input())
l2=list(map(int,input().split()))
s=0
for i in l1:
    for j in l2:
        if i==j:
            s+=1
            break
if s==a:
    print(True)
else:
    print(False)