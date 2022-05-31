#11720
import sys
a = int(sys.stdin.readline())
b = list(sys.stdin.readline().rstrip())
sum = 0
for i in range(a):
    sum += int(b[i])
print(sum)

# n = input()

# print(sum(map(int,input())))