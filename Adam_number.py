def rev(n):
    rev=0
    while n!=0:
        r=n%10
        rev=rev*10+r
        n=n//10
    return rev
n=int(input())
s=n*n
r=rev(n)
sq=r*r
a=rev(sq)
if a==s:
    print(True)
else:
    print(False)