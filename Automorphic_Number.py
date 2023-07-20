def count(n):
    c=0
    while n!=0:
        r=n%10
        c+=1
        n=n//10
    return c

n=int(input())
s=n**2
c=count(n)
if s%(10**c)==n:
    print('Automorphic Number')
else:
    print('Not an Automorphic Number')
    
    
