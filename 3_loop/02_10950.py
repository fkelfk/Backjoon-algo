#10950
from posixpath import split
a = int(input())

for i in range(a):
    b, c = map(int,input().split())
    print(b+c)
