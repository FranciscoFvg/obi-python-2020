n, m, i = [int(i) for i in input().split()]

k = []
r = []
ins = []

def troca(f1, f2):
    f1 -= 1
    f2 -= 1
    vf1 = k[f1]
    k[f1] = k[f2]
    k[f2] = vf1

def pergunta(f):
    f -= 1
    for j in range(m):
        if r[j][0] == f or r[j][0] == f:
        
    print(k[x])

for j in range(n):
    k.append(int(input()))

for j in range(m):
    r1 = []
    r1.append(int(input().split()))
    r.append(r1)

for j in range(i):
    i1 = []
    i1.append(input())
    i1.append(int(input().split))
    ins.append(i1)

for j in range(i):
    if ins[i][0] == "T":
        troca(ins[i][1], ins[i][2])
    if ins[i][0] == "P":
        pergunta(ins[i][1])


print(k)