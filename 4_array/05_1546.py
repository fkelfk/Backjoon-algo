#1546

import sys

a = int(sys.stdin.readline())
grade = list(map(int,sys.stdin.readline().split()))

new_grade = 0
for i in range(a):
    new_grade+=((grade[i]/max(grade))*100)  
print((new_grade)/a)
