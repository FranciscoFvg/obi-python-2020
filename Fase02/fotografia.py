A,L = [int(i) for i in input().split()]
n = int(input())

fa = A * L

def cabe(mold):
  if mold[0] >= A and mold[1] >= L or mold[0] >= L and mold[1] >= A:
    return True
  else:
    return False

def area(mold):
  am = mold[0] * mold[1]
  sobra = am - fa
  return sobra

m = []
for i in range(n):
  novo = [int(i) for i in input().split()]
  m.append(novo)

lc = []
for i in range(len(m)):
  if cabe(m[i]) == True:
    lc.append(i)

if not lc:
  print(-1)
else:
  lf = []
  for i in lc:
    novof = []
    novof.append(area(m[i]))
    novof.append(i+1)
    lf.append(novof)

  lf.sort()
  print(lf[0][1])