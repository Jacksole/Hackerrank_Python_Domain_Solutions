'''
Title     : Eye and Identity
Subdomain : Numpy
Domain    : Python
Author    : Ahmedur Rahman Shovon
Created   : 15 July 2016
Problem   : https://www.hackerrank.com/challenges/np-eye-and-identity/problem
'''
import numpy

if __name__ == '__main__':
    n, m = map(int, input().split())
    numpy.set_printoptions(sign=' ')
    print(numpy.eye(n, m, k=0))
