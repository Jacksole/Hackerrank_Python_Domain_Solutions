'''
Title     : String Split and Join
Subdomain : Strings
Domain    : Python
Author    : Ahmedur Rahman Shovon
Created   : 15 July 2016
Problem   : https://www.hackerrank.com/challenges/python-string-split-and-join/problem
'''


# Enter your code here. Read input from STDIN. Print output to STDOUT
def split_and_join(line):
    return "-".join(line.split())


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
