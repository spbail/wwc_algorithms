for i in range(1, 101):
    if not (i % 15):
        print "fizzbuzz"
    elif (i % 3) == 0:
        print "fizz"
    elif (i%5) ==0:
        print "buzz"
    else:
        print i
