n = int(input())
x = int(input())
y = int(input())
z = int(input())

l = [x,y,z]
l.sort()
r=0

for i in l:
    if n >= i:
        n -= i
        r += 1

print(r)