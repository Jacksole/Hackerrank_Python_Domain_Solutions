'''
Title     : Floor, Ceil and Rint
Subdomain : Numpy
Domain    : Python
Author    : Ahmedur Rahman Shovon
Created   : 15 July 2016
Problem   : https://www.hackerrank.com/challenges/floor-ceil-and-rint/problem
'''
import numpy

if __name__ == '__main__':
    np_ar = numpy.array(list(map(float, input().split())), float)
    numpy.set_printoptions(sign=' ')
    print(numpy.floor(np_ar))
    print(numpy.ceil(np_ar))
    print(numpy.rint(np_ar))
