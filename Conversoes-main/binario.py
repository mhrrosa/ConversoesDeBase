"""
Aluno:
    João Márcio Wozniack
"""

while True:
    binario = input("Digite um número binário: ")
    if binario.isnumeric():
        break
    else:
        print('VALOR INVÁLIDO!')

quantidade_digitos = len(str(binario))
soma = 0
numero_invertido = binario[::-1]
x = 0

for i in numero_invertido:
        resultado = (2 ** x)*int(i)
        soma+=resultado
        x+=1

print(soma)