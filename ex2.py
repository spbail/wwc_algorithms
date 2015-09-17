for sweep in xrange(1,101):
    for step in range(0, 100, sweep):
        l[step] = not l[step]
