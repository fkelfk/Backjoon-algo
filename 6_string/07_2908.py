# 2908

import sys

a, b = map(str, sys.stdin.readline().split())
reverse_a = ""
reverse_b = ""
for i in reversed(str(a)):
    reverse_a += i
for i in reversed(str(b)):
    reverse_b += i

print(max(reverse_a, reverse_b))
