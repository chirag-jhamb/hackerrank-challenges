Given two strings, A and B, that may or may not be of the same length, determine the minimum number of character deletions required to make A and B anagrams. Any characters can be deleted from either of the strings.
def number_needed(a, b):
    a=list(a)
    b=list(b)
    for i in range(0,len(a)):
        for j in range(0,len(b)):

            if a[i]==b[j]:
                a[i]=None
                b[j]=None

    return (len(filter(lambda x: x is not None, a))) +(len(filter(lambda x: x is not None, b)))

a = raw_input().strip()
b = raw_input().strip()

print number_needed(a, b)
