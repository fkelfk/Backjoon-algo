#1330
from operator import truediv


a, b = map(int,input().split())

if a>b:
    print(">")
elif a<b:
    print('<')
elif a==b:
    print('==')
