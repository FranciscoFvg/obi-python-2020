from fractions import gcd

N,M = [int(i) for i in input().split()]

S = ([int(i) for i in input().split()])

def mdc(l):
    newl = l
    md = gcd(newl[0],newl[1])
    if len(newl) >= 2:
        for i in range(len(newl)-2):
            md = gcd(md,newl[i+2])
    return md

def criarSubSeq(sub):
    total = 0

    for i in sub:
        if i != 1:
            total += 1

    
    for i in range(len(sub)):
        for j in range(len(sub)-i+1):
            comp = sub[i:j+i]
            if len(comp) >= 2:
                if mdc(comp) > 1:
                    total += 1;

    return total

r = []

for i in range(M):
    inp = input().split()
    T = inp[0]
    I = int(inp[1])
    E = int(inp[1])
    V = int(inp[2])
    D = int(inp[2])
    if T == '2':
        r.append(criarSubSeq(S[(E-1):(D)]))
    else:
        S[I-1] = V

for i in r:
    print(i)