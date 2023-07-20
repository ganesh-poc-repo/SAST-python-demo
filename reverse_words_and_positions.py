s=input()
l=s.split()
for i in range(-1,len(l)-2*len(l)-1,-1):
    sr=str(l[i])
    print(sr[-1::-1],end=" ")