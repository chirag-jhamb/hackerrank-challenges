#For each string, print whether or not the string of brackets is balanced on a new line. If the brackets are balanced, print YES; otherwise, print NO.
def is_matched(a):
    m=list(a)
    s=[]
    r={'(':')','{':'}','[':']'}
    for ch in m:

        if ch in r.keys():
            s.append(ch)
        elif ch in r.values() and len(s)>0:
            x=s.pop()
            if r.get(x)!=ch:
                return False
        else:
            return False
    if len(s)==0:
        return True
    else:
        return False


t = int(raw_input().strip())
for a0 in xrange(t):
    expression = raw_input().strip()
    if is_matched(expression) == True:
        print "YES"
    else:
        print "NO"
