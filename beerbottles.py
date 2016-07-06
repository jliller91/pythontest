"""
Justin Liller - 99 Bottles of Beer on the Wall
Python Practice
7-6-2016
"""

for x in range(99, 0, -1):
    if x-1 > 1:     # more than one before and after
        print("x %d bottles of beer on the wall, %d bottles of beer. Take one down and pass it around,"
              " %d bottles of beer on the wall\n" % (x, x, x-1))
    elif x-1 == 1:  # will end with 1 bottle
        print("%d bottles of beer on the wall, %d bottles of beer. Take one down and pass it around,"
              " %d bottle of beer on the wall\n" % (x, x, x - 1))
    elif x-1 == 0 or x == 0:  # 1 bottle on the wall
        print("%d bottle of beer on the wall, %d bottle of beer. Take one down and pass it around,"
              " No more bottles of beer on the wall\n" % (x, x))

print("No bottles of beer on the wall, no bottles of beer. Go to the store and buy some more, 99 "
      "bottles of beer on the wall")