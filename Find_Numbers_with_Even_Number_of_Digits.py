def count(n):
    c=0
    while n!=0:
        r=n%10
        c+=1
        n=n//10
    if c%2==0:
        return 1
    else:
        return 0

n=int(input())
l=list(map(int,input().split()))
s=0
for i in l:
    s+=count(i)
print(s)