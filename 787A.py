#######################
# python 46ms C++ 15ms#
#######################
import sys
from fractions import gcd
R=lambda:list(map(int,input.split()))
a,b=R()
c,d=R()
#a,b=[int(i) for i in input().split()]
#c,d=[int(i) for i in input().split()]
#a,b=input().split();
#c,d=input().split();
#a=int(a);
#b=int(b);
#c=int(c);
#d=int(d);

if abs(b-d)%gcd(a,c) !=0 :
    print(-1);
    exit(0);
else:
    while b!=d :
        if d>b: b=b+a;
        else: d=d+c;
    print(b);
    exit(0);
