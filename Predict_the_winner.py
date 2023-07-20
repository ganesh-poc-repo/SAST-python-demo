n=int(input())
l=list(map(int,input().split()))
s=0
for i in l:
    s+=i
if s%4==0:
    print('X')
else:
    print('Y')