#!/bin/python
#Given set S={1,2,3,...N}. Find two integers,  A and B (where A>B), from set S such that the value of A&B is the maximum possible and also less than a given integer, K. In this case, & represents the bitwise AND operator.
import sys


t = int(raw_input().strip())
def calc(x,y):
    k=0
    for i in range(1,x):
        for j in range(i+1,x):
            if ((i&j)>k) and (i&j)<y:
                k=i&j
    return k
for a0 in xrange(t):
    n,k = raw_input().strip().split(' ')
    n,k = [int(n),int(k)]
    print calc(n,k)
   
