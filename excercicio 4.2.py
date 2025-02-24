#escreva um programa que pergunte a velocidade do carro de um usuário.
# Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário foi multado.
# Nesse caso, exiba o valor da multa, cobrando R$ 5 por km acima de 80 km/h.
multa = 0
foimultado = False

velocidade = float(input("Qual a velocidade do carro? "))
if velocidade > 80:
    foimultado = True
    multa = (velocidade - 80) * 5
if foimultado: 
    print("Você foi multado em R$", multa)
else:
    print("Você está dentro do limite de velocidade")
