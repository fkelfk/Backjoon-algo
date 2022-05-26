# 3052

import sys

a=[]

for i in range(10):
    num = int(sys.stdin.readline())
    a.append(int(num % 42))

print(len(set(a)))