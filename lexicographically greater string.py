#For each testcase, output a string lexicographically bigger than 'w' in a separate line. In case of multiple possible answers, print the lexicographically smallest one, and if no answer exists, print no answer.
def largest_decreasing_sequence(l, n):
	i = n-1
	while (i >= 0) and (l[i] <= l[i-1]):
		i -= 1
	return  i


# Reverse l[i .. (n-1)]
def reverse(l, i, n):
	j = n-1
	while (i < j):
		l[i], l[j] = l[j], l[i]
		i += 1
		j -= 1

def next_lexicographic_permutation(l, n):
	i = largest_decreasing_sequence(l, n)
	if i <= 0:
		return False # No next permutation exists, this is the last permutation (lexicographically)
	pivot = l[i-1]
	# From R-L, find first element in 'suffix'
	j = n-1
	while (j >= i) and (l[j] <= pivot):
		j -= 1
	# Swap l[i-1] and l[j]
	l[i-1], l[j] = l[j], l[i-1]
	# Reverse the 'suffix'
	reverse(l, i, n)
	return True
n = int(raw_input())
for i in xrange(n):
	l = map(ord, raw_input().strip())
	ln = len(l)
	print ''.join(map(chr, l)) if next_lexicographic_permutation(l, ln) else 'no answer'
