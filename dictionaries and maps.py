#Given n names and phone numbers, assemble a phone book that maps friends' names to their respective phone numbers. You will then be given an unknown number of names to query your phone book for. For each name queried, print the associated entry from your phone book on a new line in the form name=phoneNumber; if an entry for name is not found, print Not found instead.
import sys
d={}
j=int(raw_input().strip())
for x in range(1,j+1):
    a,b=map(str, raw_input().split())
    d[a]=str(b)


while True:
    try:
        l = raw_input()
    except EOFError:
        break
    try:
        print l +"="+d[l]
    except KeyError:
        print "Not found"
