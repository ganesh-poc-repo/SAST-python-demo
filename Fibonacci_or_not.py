n=int(input())
a,b=0,1
for i in range(2,n):
    c=a+b
    if c==n:
        print(True)
        break
    a=b
    b=c
else:
    print(False)
