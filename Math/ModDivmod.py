'''
Title     : Mod Divmod
Subdomain : Math
Domain    : Python
Author    : Ahmedur Rahman Shovon
Created   : 15 July 2016
Problem   : https://www.hackerrank.com/challenges/python-mod-divmod/problem
'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    d = divmod(a, b)
    print(d[0])
    print(d[1])
    print(d)
