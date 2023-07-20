a,b,c=map(int,input().split())
c=2*a*b*c*512
t=c//1024
print(t,end="")
print('KB')