__author__ = 'dan'
import sys
sys.setrecursionlimit(10000)

def factor(n):
    if n == 1:
        return 1
    else:
        return factor(n-1) * n

def reverse(s):
    if len(s) <= 1:
        return s
    else:
        return reverse(s[1:]) + s[0]

def fast_power(a, n):
    if n == 0:
        return 1
    elif n % 2 == 1:
        return fast_power(a, n - 1) * a
    else:
        tmp = fast_power(a, n//2)
        return tmp * tmp

def Hanoi(n, start, finish):
    if n == 1:
        print("Disk 1 from {} to {}".format(start, finish))
    else:
        tmp = 6 - start - finish
        Hanoi(n - 1, start, tmp)
        print("Disk {} from {} to {}".format(n, start, finish))
        Hanoi((n - 1, tmp, finish))

print(factor(10))