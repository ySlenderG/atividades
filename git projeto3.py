import time
tempo = input("Digite o tempo (em segundos): ")

#esse if e para ter a confimacao que ele digitou numero
if tempo.isdigit():
    tempo = int(tempo)
else:
    print("Entrada invalida!")
    quit()

# 120 / 60 = 2
# 150 / 60 = 2 | 30
while tempo != 0:    
    minutos, segundos = divmod(tempo, 60)
    timer = "{:02d}:{:02d}".format(minutos, segundos)
    print(timer, end="\r")
    time.sleep(1)
    tempo = tempo - 1

print("TEMPO ACABOU !!!!!!!!!!!")