#!/bin/python
#Given a base-10 integer,n , convert it to binary (base-2). Then find and print the base-10 integer denoting the maximum number of consecutive 1's in n's binary representation.
import sys
n = int(raw_input().strip())
x=str(bin(n))[2:]
p=0
m=0
for i in x:
    if i=='1':
        p=p+1
        if m<p:
            m=p
    else:
        p=0
print m
