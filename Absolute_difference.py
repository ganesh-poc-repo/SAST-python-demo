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
p=1
m=1
for i in l:
    if prime(i):
        p*=i
    else:
        m*=i
print(abs(m-p))