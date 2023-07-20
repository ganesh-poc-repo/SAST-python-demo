import math
p,r,t=map(float,input().split())
d=math.pow((1+(r/100)),t);
ci=p*d
print("%.2f"%ci)