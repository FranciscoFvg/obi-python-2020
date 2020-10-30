dicionario = {}

#Incremento de itens em um dicionário através de input
for i in range(2):
    en1 = input('nova coluna')
    dicionario[en1] = input().split()

print(dicionario)