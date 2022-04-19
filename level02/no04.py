
# while True:
#     x = int(input())
#     if -1000 <= x <= 1000 and x != 0:
#         break
#     else:
#         print("x좌표는 0이아닌 -1000에서 1000사이의 정수를 입력하세요")

# while True:
#     y = int(input())
#     if -1000 <= y <= 1000 and y != 0:
#         break
#     else:
#         print("y좌표는 0이아닌 -1000에서 1000사이의 정수를 입력하세요")

while True:
    x = int(input()) 
    y = int(input())
    if -1000 <= x <= 1000 and x != 0 and -1000 <= y <= 1000 and y != 0 :
        if x > 0 and y > 0 :
            print("1")
        elif x > 0 and y < 0 :
            print("4")
        elif x < 0 and y < 0 :
            print("3")
        else :
            print("2")
        break
    else:
        print("좌표는 0이아닌 -1000에서 1000사이의 정수를 입력하세요")