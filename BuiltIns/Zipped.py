'''
Title     : Zipped!
Subdomain : Built-Ins
Domain    : Python
Author    : Ahmedur Rahman Shovon
Created   : 15 July 2016
Problem   : https://www.hackerrank.com/challenges/zipped/problem
'''

import statistics

n, x = map(int, input().split())
l1 = [map(float, input().split()) for i in range(x)]

if __name__ == '__main__':
    for i in list(zip(*l1)):
        print(statistics.mean(i))
