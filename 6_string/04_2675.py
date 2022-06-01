#2675
import sys
t = int(sys.stdin.readline())

for i in range(t):
    r, s = map(str,sys.stdin.readline().split())
    p = ''
    for m in s:
        p += int(r)*m
    print(p)