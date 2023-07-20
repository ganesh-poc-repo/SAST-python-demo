a,b=map(int,input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
print(len(set(l1) & set(l2)))