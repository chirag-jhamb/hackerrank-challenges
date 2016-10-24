#input is the submission and due date. Charge 15 hackos for per day, 500 hackos for per month if late, and 10000 hackos if not of same year.
import sys
def calc(sub,due,rate):
    print (sub-due)*rate

d1,m1,y1=map(int, raw_input().split())
d2,m2,y2=map(int, raw_input().split())
if y1>y2:
    print 10000
elif m1>m2 and y2==y1:
    calc(m1,m2,500)
elif d1>d2 and m1==m2:
    calc(d1,d2,15)
else:
    print 0
