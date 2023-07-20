def div(i):
    n=i
    while i!=0:
        r=i%10
        if r!=0 and n%r==0:
            i=i//10
        else:
            return -1
    return n

a=int(input())
b=int(input())
for i in range(a,b+1):
    if i<10:
        print(i,end=" ")
    else:
        if div(i)==-1:
            continue
        else:
            print(div(i),end=" ")