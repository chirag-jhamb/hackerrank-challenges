#Given an array, Find and print the number of pairs where Ai + Aj (i>j) is evenly divisible by input k.
import sys
n,k = raw_input().strip().split(' ')
n,k = [int(n),int(k)]
a = map(int,raw_input().strip().split(' '))
c=0
for i in range(0,n):
    for j in range(i+1,n):
        if (a[i]+a[j])%k==0:
            c=c+1
print c
