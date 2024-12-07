import random

print("Seja muito bem vindo ao jogo de numero!")
choice_number = input("Digite um nomero para o desafio (lembrando quando mais numero mais dificil fica): ")

if choice_number.isdigit():
    choice_number = int(choice_number)
else:
    print("Erro: Valor informado não é numero. favor executar novamente!")
    quit()
    
random_number = random.randint(0, choice_number)

n_choices = 0

while True:
    answer_user = input("Adivinha o numero: ")

    if answer_user.isdigit():
        answer_user = int(answer_user)
    else:
        print("Erro: o valor informado nao e numerico, favor informe um numero!")
        continue

    n_choices = n_choices + 1

    if answer_user == random_number:
        print("Acertou!")
        break

print("Nº de tentativas:"  + str(n_choices))