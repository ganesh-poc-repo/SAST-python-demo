n=input()
c="!@#$%^&*()-_=+[]{};:'"\|<>,.?/~`"
s=0
for i in n:
    if i in c:
        s+=1
print(s)