#8958
import sys

a = int(sys.stdin.readline())
for i in range(a):
    b = list(str(sys.stdin.readline().strip()))
    sum = 0
    c = 1
    for w in range(len(b)):
        if b[w] == "O":
            sum += c
            c += 1
        else:
            c = 1
    print(sum)

