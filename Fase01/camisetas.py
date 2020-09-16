n = int(input())

t = []
t = input().split()

p = int(input())
m = int(input())

rp = 0
rm = 0
for i in t:
    if int(i) == 1:
        rp += 1
    else:
        rm += 1

if p >= rp and m >= rm:
    print('S')
else:
    print('N')