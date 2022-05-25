#1110
import sys
    

N = int(sys.stdin.readline())

new = N
count = 0

while(new != N or count == 0):
    ones = new % 10
    tens = new // 10
    s = ones + tens
    new = int(str(ones)+str(s%10))
    count += 1

print(count)


