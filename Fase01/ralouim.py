palacio = [0,0]
disLimite = 11000
guloseima = 0

def dis2pontos(p1, p2):
    d = pow((p2[0] - p1[0])**2+(p2[1] - p1[1])**2)
    return d

def maisDislimite(partida, limite, tendas):
    grupo = []
    for i in tendas:
        dis = 0.0
        dis = dis2pontos(partida, i)
        grupo.append(dis)
    grupo.sort()
    grupo.reverse()
    for i in grupo:
        if i < limite:
            limite = grupo[i]
            guloseima += 1
            return 


n = int(input())
t = []
for i in range(n):
    pon = input().split()
    t.append(pon)

