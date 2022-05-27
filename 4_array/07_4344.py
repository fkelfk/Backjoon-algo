#4344
import sys

case = int(sys.stdin.readline())

for i in range(case):
    sum = 0
    upper = 0
    grade = list(sys.stdin.readline().split())
    for w in range(int(grade[0])):
        sum+=int(grade[w+1])
    for t in range(int(grade[0])):
        if int(grade[(t+1)]) > int(int(sum)/int(grade[0])):
            upper += 1
    result=float(float(upper)/float(int(grade[0]))) 
    print(f"{'%0.3f' % (result * 100)}%")

