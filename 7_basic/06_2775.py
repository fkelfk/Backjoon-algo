#  2775

# 1층의 3호에 살려면
# 아래 0층의 1호부터 3후까지 사람들의 수의 합만큼

# 001 002 003
# 1명  2명  3명 = 6

# 2층의 3호에 살려면
# 1층의


# 1 3 6 = 10
# 1 2 3


# 1 6 21
# 1 5 15
# 1 4 10
# 1 3 6
# 1 2 3


import sys

case = int(sys.stdin.readline())

for i in range(case):
    floor = int(sys.stdin.readline())
    room = int(sys.stdin.readline())
    roomlist = [x for x in range(1, room + 1)]
    for k in range(floor):
        for j in range(1, room):
            roomlist[j] += roomlist[j - 1]
    print(roomlist[-1])
