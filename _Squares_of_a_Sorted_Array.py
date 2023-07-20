n=int(input())
l=list(map(int,input().split()))
sq=[]
for i in l:
    sq.append(i**2)
sq.sort()
for j in sq:
    print(j,end=" ")