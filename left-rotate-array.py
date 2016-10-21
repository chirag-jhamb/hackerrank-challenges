#A left rotation operation on an array of size N shifts each of the array's elements 1 unit to the left
import sys
i,j=map(int, raw_input().split())
x=[]
x = [int(a) for a in raw_input().split()]
p=x[:j]
x=x[j:]
x.extend(p)
print ' '.join(map(str, x))
