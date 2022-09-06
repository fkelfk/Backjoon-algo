# 1316

import sys

num = int(sys.stdin.readline())
cnt = num
for i in range(num):
    word = list(map(str, sys.stdin.readline().strip()))
    for i in range(len(word) - 1):
        if word[i] == word[i + 1]:
            pass
        elif word[i] in word[i + 1:]:
            cnt -= 1
            break

print(cnt)
