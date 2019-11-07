'''
Title     : Alphabet Rangoli
Subdomain : Strings
Domain    : Python
Author    : Ahmedur Rahman Shovon
Created   : 15 July 2016
Problem   : https://www.hackerrank.com/challenges/alphabet-rangoli/problem
'''
import string

def print_rangoli(size):
    width = 4 * size - 3
        alpha = string.ascii_lowercase
        for i in list(range(size))[::-1] + list(range(1, size)):
            print('-'.join(alpha[size-1:i:-1] + alpha[i:size]).center(width, '-'))


if __name__ == '__main__':
    n  = int(input())
    print_rangoli(n)