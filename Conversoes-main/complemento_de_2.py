'''
Aluno:
    João Márcio Wozniack
'''

b1 = []
b2 = []
while True:
    primeiro_binario = input("Digite um número binário: ")
    segundo_binario = input("Digite outro número binário: ")
    tamanho1 = len(primeiro_binario)
    tamanho2 = len(segundo_binario)
    if tamanho1 < tamanho2:
        print("Valores incorretos, digite novamente")
        continue
    else:
        break

for i in primeiro_binario:
    b1.append(int(i))

for i in segundo_binario:
    b2.append(int(i))
    while len(b2) + tamanho2 <= len(b1):
        b2.insert(0, 0)

b2_invertido = []
for i in b2:
    if i == 0:
        i = 1
    else:
         i = 0
    b2_invertido.append(i)

b1_invertido = list(reversed(b1))
b2_invertido = list(reversed(b2))
posicao = 0
sobra = 0
lista_resposta =[]
for binario1 in b1_invertido:

    binario2 = int(b2_invertido[posicao])

    if sobra == 1 and binario1 == 1 and binario2 == 1:
        resposta = 1
        sobra = 1

    elif sobra == 1 and binario1 == 0 and binario2 == 1 or sobra == 1 and binario1 == 1 and binario2 == 0:
        resposta = 0
        sobra = 1
    elif sobra == 0 and binario1 == 1 and binario2 == 1:
        resposta = 0
        sobra = 1
    elif binario1 == 1 and binario2 == 0 or binario1 == 0 and binario2 == 1 or sobra == 1 and binario1 == 0 \
            or sobra == 1 and binario2 == 0 :
        resposta = 1
        sobra = 0
    elif binario1 == 0 and binario2 == 0:
        resposta = 0
        sobra = 0
    else:
        break
    posicao+=1
    lista_resposta.append(resposta)

if sobra == 1:
    lista_resposta.append(1)

resposta_final = list(reversed(lista_resposta))
print('binario 1: ',b1)
print('binario 2: ',b2)
print('resposta: ',resposta_final)