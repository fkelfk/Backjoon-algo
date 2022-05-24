#10952

import sys

while True:
    a, b = map(int,sys.stdin.readline().split())
    if a+b != 0:
        print(a+b)
    elif a+b == 0:
        break
