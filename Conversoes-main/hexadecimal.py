"""
Aluno:
    João Márcio Wozniack
"""

letras_hexadecimal = {"A" : 10,
                      "B" : 11,
                      "C" : 12,
                      "D" : 13,
                      "E" : 14,
                      "F" : 15}

while True:
    hexadecimal = input("Digite um número hexadecimal: ")
    if hexadecimal.isalnum():
        for i in hexadecimal.upper():
            if i.isnumeric():
                continue
            elif i in (letras_hexadecimal.keys()):
                continue
            else:
                print("VALOR INVÁLIDO")
                hexadecimal = input("Digite um número hexadecimal: ")
        break
    else:
        print('VALOR INVÁLIDO!')

quantidade_digitos = len(str(hexadecimal))
soma = 0
numero_invertido = hexadecimal[::-1].upper()
x = 0

for i in numero_invertido:
    if i.isalpha():
        i = letras_hexadecimal[i]
    resultado = (16 ** x)*int(i)
    soma+=resultado
    x+=1

print(soma)