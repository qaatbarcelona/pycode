#!/usr/bin/python
import sys
import random

# This function prints the nth element of a random integer list
# Can be called with params:
# 1st param num of random integers (5000 by default)
# 2nd param nth smallest integer to be printed (8 by default)
# max value for the integers is sys.maxsize

def main():

    randomList = list()

    if len(sys.argv) >= 3:
        listLength = int(sys.argv[1])
        print("Creating " + str(listLength) + " random integers with max value: " + str(sys.maxsize))
        nElement = int(sys.argv[2])
        print("Will print smallest integer at position: " + str(nElement))
    else:
        print("Creating 5000 random integers, set different value as first param, with max value: " + str(sys.maxsize))
        listLength = 5000
        print("Will print 8th smallest value, set different position as second param")
        nElement = 8

    for x in range(0, listLength):
        randomList.append(random.randint(0, sys.maxsize))

    sortedList=sorted(randomList)

    print("Result: " + str(sortedList[nElement-1]))


if __name__ == '__main__':
    main()