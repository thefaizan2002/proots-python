from __future__ import division

#-------------------------------------------------------------------------------
# Name:        Primitive Roots Calculator
# Range:       This algo can calculate the primitive roots of
#              first 10000 prime numbers
#
# Author:      Faizan Afzal
# Email:       thefaizan@gmail.com 
# Created:     03/12/2014
# Copyright:   (c) Faizan Afzal 2014
# Licence:     This is an open source program licensed under the
#              [MIT license](http://opensource.org/licenses/MIT)
#-------------------------------------------------------------------------------


def main():
    pass

if __name__ == '__main__':
    main()

import math
import cmath

def isNotPrime(number):

    i = 2
    while (i<=math.sqrt(number)):
        if (math.floor(number/i) == (number/i)):
            return True
        i += 1
    return False

def proots(number):
    if (isNotPrime(number)):
        return "The entered number is not a Prime number"

    o = 1
    k = True
    result = True
    roots = []
    z = 0

    r = 2
    while (r<number): # the number must be greater than 2
        k = math.pow(r,o)
        k = k%number

        while (k>1): #increasing the power of 'r' which is 'o'
            o += 1
            k *= r
            k = k%number

        if (o == (number-1)):
            roots.append(r)
            z += 1

        o = 1
        r += 1
    result = "The number %d has %d primitive roots and they are " %(number,z)
    z -= 1

    y = 0
    while(y<z):
        result += "%s, " %(roots[y])
        y += 1

    result += "and %s" %(roots[z])

    return result


number = input("Please enter the prime no: ")

if (math.floor(number) != number): #number must be a natural number
    print "Please enter a valid Prime number"

elif (number <= 2): #number must be greater than 2
    print "The prime number must be greater than 2"
else:
    print proots (number)
