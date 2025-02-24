#Analise o programa da listagem 4.2 e responda o que acontece se o primeiro e o segundo número forem iguais?
# Explique.
a = int(input("Primeiro número: "))
b = int(input("Segundo número: "))
if a > b:
    print(a)
if b > a:
    print(b)
# Se os números forem iguais, o programa irá imprimir o segundo número,
# pois o programa não tem uma condição para números iguais.
# O programa só tem condições para números diferentes.
a = int(input("Primeiro número: "))
b = int(input("Segundo número: "))  
if a > b:
    print(a)
if b > a:
    print(b)
if a == b:
    print("Os números são iguais")
# Neste caso, o programa irá imprimir a mensagem "Os números são iguais" se os números forem iguais.
# Pois foi adicionado uma condição para números iguais.
