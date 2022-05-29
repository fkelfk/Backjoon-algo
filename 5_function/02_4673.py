# 4673

a = set(range(1,10001))
b = set()

for i in range(1,10001):
    for j in str(i):
        i += int(j)
    b.add(i)

self = sorted(a-b)
for i in self:
    print(i)    