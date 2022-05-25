#2884
while True:
    h, m  = map(int,input().split())
    if 0 <= h <= 23 and 0 <= m <= 59:
        if h == 0 and m < 44:
            print(23, 60+(m-45))
        elif h == 0 and m > 44:
            print(h, m-45)    
        elif h > 0 and m < 44:
            print(h-1, 60+(m-45))
        elif h > 0 and m >44:
            print(h, m-45)
        break
    else:
        print("h는 0에서 23까지 m은 0에서 59까지 입력하세요")
        