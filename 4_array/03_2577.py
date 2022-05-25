# import sys

# a = int(sys.stdin.readline())
# b = int(sys.stdin.readline())
# c = int(sys.stdin.readline())
# d = list(str(a*b*c))

# for i in range(10):
#     print(d.count(str(i)))

n=1
for i in range(3):
    n *= int(input())
for i in range(0,10): 
    print(str(n).count(str(i)))

