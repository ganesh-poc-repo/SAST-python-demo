a=int(input())
b=int(input())
s=0
for i in range(1,a):
    if a%i==0:
        s+=i
c=0
for j in range(1,b):
    if b%j==0:
        c+=j
if s==b and c==a:
    print("Amicable")
else:
    print("Not Amicable")