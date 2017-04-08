#######################
# python 46ms C++ 15ms#
#######################
import sys
#a,b =map(int, sys.stdin.readline().split())
#input_user=map(int,raw_input().strip().split(" "))
a,b=raw_input().split();
a=int(a);
b=int(b);
n=0;
while (a<=b):
    a=a*3;
    b=b*2;
    n=n+1;

print(n);
