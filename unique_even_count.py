n=int(input())
a=list(map(int,input().split()))
l=list(set(a))
s=0
for i in l:
    if i%2==0:
        s+=1
print(s)