# 1193
import sys

num = int(sys.stdin.readline())
cnt = 0

while num - cnt > 0:
    num -= cnt
    cnt += 1

a = cnt - num + 1

if cnt % 2 == 0:
    print(f"{num}/{a}")

else:
    print(f"{a}/{num}")
