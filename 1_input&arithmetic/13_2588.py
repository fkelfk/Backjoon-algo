#2588

a = int(input())
b = input()

# print(a*int(b[2]))
# print(a*int(b[1]))
# print(a*int(b[0]))
# print(a*int(b))

for i in reversed(b):
    print(a*int(i))
print(a*int(b))

