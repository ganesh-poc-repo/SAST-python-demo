def adddigits(n):
    s=0
    while(n!=0):
        r=n%10
        s+=r
        n=n//10
    return s
        
n=int(input())
while(1):
    if n<10:
        print(n)
        break
    else:
        n=adddigits(n)