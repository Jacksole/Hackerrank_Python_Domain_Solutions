'''
Title     : Find the Second Largest Number
Subdomain : Data Types
Domain    : Python
Author    : Ahmedur Rahman Shovon
Created   : 15 July 2016
Problem   : https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    n = int(input())
    num_str_ar = input().strip().split()
    num_ar = list(map(int, num_str_ar))
    set_tmp = set(num_ar)
    final_ar = list(set_tmp)
    final_ar.sort()
    print(final_ar[-2])
