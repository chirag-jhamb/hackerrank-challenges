#"A child is running up a staircase with n steps and can hop either 1 step, 2 steps or 3 steps at a time. Implement a method to count how many possible ways the child can run up the stairs.
def func(x):
    if x==0 or x==1:
        return 1
    p=0
    p3=0
    p2=1
    p1=1
    for i in range(n-1):
        p=p3+p2+p1
        p3=p2
        p2=p1
        p1=p
    return p
s = int(raw_input().strip())
for a0 in xrange(s):
    n = int(raw_input().strip())
    print func(n)
