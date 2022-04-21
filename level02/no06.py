#2525
a, b= map(int,input().split())
c = int(input())
d = (b+c)%60    
e = (b+c)//60   

if a+e>23:
    print((a+e)-24, d) 
elif a+e<=23:
    print((a+e), d)


# short

# h,m,t=map(int,open(0).read().split())
# m+=t
# print((h+m//60)%24,m%60)