"""
Title     : Validating Credit Card Numbers
Subdomain : Regex and Parsing
Domain    : Python
Author    : Ahmedur Rahman Shovon
Created   : 15 July 2016
Problem   : https://www.hackerrank.com/challenges/validating-credit-card-number/problem

You and Fredrick are good friends. Yesterday, Fredrick received  credit cards from ABCD Bank.
He wants to verify whether his credit card numbers are valid or not.
You happen to be great at regex so he is asking for your help!

A valid credit card from ABCD Bank has the following characteristics:

► It must start with a ,  or .
► It must contain exactly  digits.
► It must only consist of digits (-).
► It may have digits in groups of , separated by one hyphen "-".
► It must NOT use any other separator like ' ' , '_', etc.
► It must NOT have  or more consecutive repeated digits.

Examples:

Valid Credit Card Numbers

4253625879615786
4424424424442444
5122-2368-7954-3214
Invalid Credit Card Numbers

42536258796157867       #17 digits in card number → Invalid
4424444424442444        #Consecutive digits are repeating 4 or more times → Invalid
5122-2368-7954 - 3214   #Separators other than '-' are used → Invalid
44244x4424442444        #Contains non digit characters → Invalid
0525362587961578        #Doesn't start with 4, 5 or 6 → Invalid
"""

import re


def is_it_valid(n):
    for t in range(n):
        credit = input().strip()
        credit_removed_hiphen = credit.replace('-', '')
        valid = True
        length_16 = bool(re.match(r'^[4-6]\d{15}$', credit))
        length_19 = bool(re.match(r'^[4-6]\d{3}-\d{4}-\d{4}-\d{4}$', credit))
        consecutive = bool(re.findall(r'(?=(\d)\1\1\1)', credit_removed_hiphen))
        if length_16 == True or length_19 == True:
            if consecutive == True:
                valid = False
        else:
            valid = False
        if valid == True:
            print('Valid')
        else:
            print('Invalid')


if __name__ == '__main__':
    n: int = int(input())
    is_it_valid(n)
