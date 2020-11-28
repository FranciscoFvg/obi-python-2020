#Resolvido após o prazo

def ordem(l = []):
    s1 = int(l[0])
    s2 = int(l[1])
    if saloes[s1-1] > saloes[s2-1]:
        return l
    else:
        newl = [l[1]] + [l[0]]
        return newl

def Encontrar_todos_caminhos(grafico, inicio, fim, caminho=[]):
    caminho = caminho + [inicio]

    if inicio == fim:
        return [caminho]

    if inicio not in grafico:
        return []

    caminhos = []

    for no in grafico[inicio]:
        if no not in caminho:
            novocaminhos = Encontrar_todos_caminhos(grafico, no, fim, caminho)
            for novocaminho in novocaminhos:
                caminhos.append(novocaminho)
                    
        return caminhos

s, t, p = [int(i) for i in input().split()]

saloes = [int(i) for i in input().split()]

grafico = {}
for i in range(t):
    l = input().split()
    l = ordem(l)
    if l[0] in grafico:
        grafico[l[0]].append(l[1])
    else:
        grafico[l[0]] = []
        grafico[l[0]].append(l[1])

c=0
for i, v in enumerate(saloes):
    if v == min(saloes):
        c = i + 1

possibilidades = Encontrar_todos_caminhos(grafico, str(p), str(c))

possibilidades.sort(reverse=True)

print(len(possibilidades[0]) - 1)