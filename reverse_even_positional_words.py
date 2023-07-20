s=input()
l=s.split()
for i in range(0,len(l)):
    sr=str(l[i])
    if i==0 or i%2==0:
        print(sr[-1::-1],end=" ")
    else:
        print(sr,end=" ")