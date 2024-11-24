salario = float(input("informe o valor do salario: "))
porcento = float(input("Informe o percentual de aumento: "))
aumento = salario * (porcento/100)
salario += aumento
print("O aumento foi de R$%5.2f e o novo salario é R$%7.2f" %(aumento, salario))