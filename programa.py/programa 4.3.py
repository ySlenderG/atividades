#exermplo de cálculo do imposto de renda
salario = float(input("Qual o seu salário? "))
base = salario
imposto = 0
if base > 3000:
    imposto = salario + ((base - 3000) * 0.35)
    base = 3000
if base > 1000:
    imposto = imposto + ((base - 1000) * 0.20)
print(f"salario: R${salario:6.2f} imposto a pagar: R${imposto:6.2f}")
# O programa calcula o imposto a pagar de acordo com o salário do usuário.
# Se o salário for maior que 3000, o imposto é igual a 35% do salário.
# Se o salário for maior que 1000, o imposto é igual a 20% do salário.
