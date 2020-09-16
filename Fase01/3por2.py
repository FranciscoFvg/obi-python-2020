pagar = 0

def pgrupo(g):
    if len(tres) == 1:
        return g[0]
    else:
        return g[0] + g[1]

n = int(input())

p = []
for i in range(n):
    p.append(int(input()))

p.sort()
p.reverse()

tres = []
cont = 0
for i in range(n):
    if cont < 3:
        tres.append(p[i])
        cont += 1     
    if cont == 3:
        pagar += pgrupo(tres)
        tres = []
        cont = 0
    if cont > 0 and (i+1) == n:
        pagar += pgrupo(tres)

print(pagar)
    