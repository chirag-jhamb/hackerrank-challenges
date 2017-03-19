#Princess Peach is trapped in one of the four corners of a square grid. You are in the center of the grid and can move one step at a time in any of the four directions. Can you rescue the princess?

def displayPathtoPrincess(n,grid):
    cr=int((n-1)/2)
    cl=int((n-1)/2)
    r=-1
    l=-1
    for i in range(n):
        if "p" in grid[i]:
            r=grid[i].index("p")
            l=i
    while (r!=cr):
        if r>cr:
            print "RIGHT"
            cr=cr+1
        else:
            print "LEFT"
            cr=cr-1
    while (l!=cl):
        if l<cl:
            print "UP"
            cl=cl-1
        else:
            print "DOWN"
            cl=cl+1
#print all the moves here
m = input()

grid = []
for i in xrange(0, m):
    grid.append(raw_input().strip())

displayPathtoPrincess(m,grid)
