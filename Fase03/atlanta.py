A = float(input())
B = float(input())

area = A + B

c = round(area**0.5)
l = area/c

t1 = l * 10
t2 = int(l) * 10

if t1 == t2:
    l = int(l)
    print("{} {}".format(c, l))
else:
    print("{} {}".format('-1', '-1'))

