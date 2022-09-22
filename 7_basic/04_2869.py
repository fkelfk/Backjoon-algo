# 2869

import sys
import math

day, night, top = map(int, sys.stdin.readline().split())

count = (top - night) / (day - night)

print(math.ceil(count))
