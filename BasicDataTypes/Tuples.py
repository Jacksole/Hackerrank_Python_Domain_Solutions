'''
Title     : Tuples
Subdomain : Data Types
Domain    : Python
Author    : Ahmedur Rahman Shovon
Created   : 15 July 2016
Problem   : https://www.hackerrank.com/challenges/python-tuples/problem
'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
numbers = input().strip().split()
ar = []

if __name__ == '__main__':
    for i in range(0, len(numbers)):
        ar.append(int(numbers[i]))
    t = tuple(ar)
    print(hash(t))
