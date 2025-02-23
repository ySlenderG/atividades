#escreva um programa que calcule a reducao de tempo de vida de um fumante.
# Pergunte a quantidade de cigarros fumados por dia e quantos anos ele ja fumou.
# Considere que um fumante perde 10 minutos de vida a cada cigarro,
# calcule quantos dias de vida um fumante perdera. Exiba o total em dias.

quantidade_de_cigarros = int(input("Quantos cigarros você fuma por dia?"))
quantos_anos = float(input("Há quantos anos você fuma?"))

quantidade_de_cigarros_total = quantos_anos * 365 * quantidade_de_cigarros
tempo_perdido_minutos = quantidade_de_cigarros_total * 10
tempo_perdido_dias = tempo_perdido_minutos / (24 * 60)
print("Você perdeu %d dias de vida" % tempo_perdido_dias)