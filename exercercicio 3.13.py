#escreva um programa que converta uma temperatura digitada em Celsius para Fahrenheit.
# A fórmula para essa conversão é: F = (9 * C / 5) + 32, sendo F a temperatura em Fahrenheit e C a temperatura em Celsius.
tempC = float(input("Digite a temperatura em ºC: "))
tempF = (9 * tempC / 5) + 32
print("%3.1fºC e igual a %3.1fºf" %(tempC, tempF))