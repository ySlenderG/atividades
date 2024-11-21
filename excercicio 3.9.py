dia = int(input("Digite a quantidade de dia: "))
horas = int(input("Digite a quantidade de horas: "))
minutos = int(input("Digite a quantidade de munutos: "))
segundos = int(input("Digite a quantidade de segundos: "))

total = segundos + 60*minutos + 60*60*horas + 24*60*60*dia

print(f"o tempo em segundos sera de {total}" )
