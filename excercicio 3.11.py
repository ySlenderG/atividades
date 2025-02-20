#faça um programa que solicite o preço de uma mercadoria e o percentual de desconto.
# Exiba o valor do desconto e o preço a pagar. vamos ver 

preco = float(input("Digite o preço da mercadoria?: "))
p_desconto = float(input("Digite o percentual de desconto: "))

desconto = preco * p_desconto / 100
preco_final = preco - desconto

print("Desconto deR$ %4.2f. Preço final: R$ %6.2f" % (desconto, preco_final))
