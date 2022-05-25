#10818
#max,min

import sys

a = int(sys.stdin.readline())
b = list(map(int,sys.stdin.readline().split()))

b.sort()
print(b[0],b[a-1])
