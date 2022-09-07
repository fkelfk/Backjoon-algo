# 1712
import sys

fixed_cost, variable_cost, cost = map(int, sys.stdin.readline().split())

if variable_cost >= cost:
    print(-1)
else:
    print((fixed_cost // (cost - variable_cost)) + 1)
