#######################
# python 46ms C++ 15ms#
#######################
import sys;
n,m=map(int, input().split())
p=0
for i in range(m):
    k,*l=map(int, input().split())
    l=set(l)
    p=0;
    for x in l:
        if -x in l :p=1; break;
    if p==0: print("Yes"); exit(0);
print("NO")

'''#####################################################

# this code is faster than mine, use intersect######
n, m = [int(w) for w in raw_input().split()]

for i in range(m):
    v = [int(w) for w in raw_input().split()][1:]
    r = {x for x in v if x > 0}
    m = {-x for x in v if x < 0}
    if not r.intersection(m):
        print("YES")
        exit(0)

print("NO")
'''
