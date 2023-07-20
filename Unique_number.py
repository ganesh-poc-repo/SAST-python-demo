n=int(input())
a=[]
while n!=0:
    r=n%10
    a.append(r)
    n=n//10
s=list(set(a))
if len(a)==len(s):
    print('Unique Number')
else:
    print('Not Unique Number')
    