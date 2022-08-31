# 11022

import sys

a = int(sys.stdin.readline())

for num in range(1, a + 1):
    b, c = map(int, sys.stdin.readline().split())
    print(f"Case #{num}: {b} + {c} = {b + c}")
