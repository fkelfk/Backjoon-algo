import sys

a = int(sys.stdin.readline().strip())

if a < 100:
    print (a)
elif 100 <= a <= 1000:
    sum = 99
    for i in range(100, a+1):
        j = str(i)
                
        if int(j[0])-int(j[1]) == int(j[1])-int(j[2]):
            sum += 1
    print(sum)
