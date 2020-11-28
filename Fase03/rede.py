# def verifica():

N = int(input())

l = []
for i in range(N):
    l.append(int(input()))

fi = 0

nl = []
for j in range(N):
    nl = []
    for i in l:
        if i >= fi:
            nl.append(i)
    if len(nl) != fi:
        fi += 1

if fi > min(nl):
    print(min(nl))
else:
    print(fi)