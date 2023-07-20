st=int(input())
l1=list(map(int,input().split()))
et=int(input())
l2=list(map(int,input().split()))
qt=int(input())
c=0
for i in range(0,st):
    if(qt>=l1[i] and qt<=l2[i]):
        c+=1
print(c)