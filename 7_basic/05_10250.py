# 10250

import sys
import math

case = int(sys.stdin.readline())

for i in range(case):
    total_floor, rooms, order = map(int, sys.stdin.readline().split())
    room_floor = order % total_floor
    if room_floor == 0:
        room_floor = total_floor
    room = math.ceil(order / total_floor)
    if room < 10:
        print(f"{room_floor}0{room}")
    else:
        print(f"{room_floor}{room}")



