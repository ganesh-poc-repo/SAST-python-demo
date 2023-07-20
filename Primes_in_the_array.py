def prime(n):
    c=0
    for i in range(1,n):
        if n%i==0:
            c+=1
    if c==1:
        return True
    else:
        return False
n=int(input())
l=list(map(int,input().split()))
c=0
for i in l:
    if prime(i):
        c+=1
print(c)