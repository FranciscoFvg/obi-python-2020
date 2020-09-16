n = int(input())
a = []
t = 0
d = 1

for i in range(n):
    a.append(int(input()))
    t += a[i]
    if t < 1000000:
        d += 1

print(d)