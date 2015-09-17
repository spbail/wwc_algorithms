limit = 15+1
a = [0 for i in xrange(limit)]
for i in xrange(2, limit):
	for j in xrange(i, limit):
		if j % i == 0 and j != i:
			a[j] = 1

for x,y in enumerate(a):
	if y is 0 and x > 1:
		print x, "prime"
