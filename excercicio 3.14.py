#escreva um programa que calcule o tempo de uma viagem de carro.
# Pergunte a distância a percorrer e a velocidade média esperada para a viagem.
km = float(input("Qual a distacia em km: "))
dias = int(input("Quantos dias voce pretende viajar? "))
valor = 60 * dias + 0.15 * km
print("O valor total sera de R$%d" %valor)