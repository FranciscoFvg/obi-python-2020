t = int(input())
n = int(input())

def viziMeio(dis, disA, disP):
  result = ((dis - disA) / 2) + ((disP - dis) /2)
  return result

dc = []
for i in range(n):
  d = int(input())
  dc.append(d)

dc.sort()

dv = []
c1 = dc[0] + ((dc[1] - dc[0]) / 2)
dv.append(c1)
for i in range(n - 1):
  if i != 0:
    dv.append(viziMeio(dc[i], dc[i-1], dc[i+1]))

c2 = (t - dc[-1]) + ((dc[-1] - dc[-2]) / 2)
dv.append(c2)

dv.sort()

print('%.2f' % dv[0])
  