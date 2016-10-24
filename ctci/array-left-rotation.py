#Given an array of N integers and a number, D, perform D left rotations on the array. Then print the updated array as a single line of space-separated integers.

def array_left_rotation(a, n, k):
    x=a[0:k]
    a=a[k:n]
    a.extend(x)
    return a
n, k = map(int, raw_input().strip().split(' '))
a = map(int, raw_input().strip().split(' '))
answer = array_left_rotation(a, n, k);
print ' '.join(map(str,answer))
