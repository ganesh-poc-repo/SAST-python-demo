n=int(input())
t=n
for i in range(0,n):
    for j in range(0,n):
        if i==j or j==t-1:
            print('x',end="")
        else:
            print('0',end='')
    t=t-1
    print()