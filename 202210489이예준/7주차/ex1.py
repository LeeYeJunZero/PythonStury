def printArgumnets(x, y, z):
    print("x=%d, y=%d, z=%d" % (x, y, z))
    sum = x + y + z
    print("x+y+z=%d" % sum)
printArgumnets(10, 20, 30)
printArgumnets(y=100, z=200, x=300)
printArgumnets(z=2000, y=1000, x=3000)