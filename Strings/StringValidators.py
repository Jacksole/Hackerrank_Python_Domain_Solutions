'''
Title     : String Validators
Subdomain : Strings
Domain    : Python
Author    : Ahmedur Rahman Shovon
Created   : 15 July 2016
Problem   : https://www.hackerrank.com/challenges/string-validators/problem
'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
inputStr=input()
resalnum = False
resalpha = False
resdigit = False
reslower = False
resupper = False

if __name__ == '__main__':
    for i in inputStr:
        if(i.isalnum()):
            resalnum=True
        if(i.isalpha()):
            resalpha=True
        if(i.isdigit()):
            resdigit=True
        if(i.islower()):
            reslower=True
        if(i.isupper()):
            resupper=True
    
    print(resalnum)
    print(resalpha)
    print(resdigit)
    print(reslower)
    print(resupper)
