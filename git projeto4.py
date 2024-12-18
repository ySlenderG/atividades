#importa da biblioteca do python o random e string
#O random para deixar a funcao ou a escolha aleatoria.
import random
#O string e para facilita para que nao precisa colocar todos os caracteres manual
#ele ja tem tudos promtos.
import string

print("gerador de senha automatico")

def password_generator(len_pass = 8):
    ascii_options = string.ascii_letters
    number_options = string.digits
    punt_options = string.punctuation
    options = ascii_options + number_options + punt_options

    password_user = ""

    for i in range(0, len_pass):
        digit = random.choice(options)
        password_user = password_user + digit

    return password_user

choice_user = input("Quantos digitos na senha?")

if choice_user.isdigit():
    choice_user = int(choice_user)
else:
    print("Entrada invalida!")
    quit()

response = password_generator(len_pass = choice_user)
print(f"senha gerada. \n{response} \n obrigado, ate mais")