n=int(input())
l=list(map(int,input().split()))
x=int(input())
a=[]
for i in l:
    if i+x>=max(l):
        a.append(True)
    else:
        a.append(False)
for i in a:
    print(i,end=" ")
        