print("bem vindo!")
answer_user = input("quer comecar? (S/N) ")

if answer_user != "S":
    print("ate mas.")
    quit()

score = 0

print("começando...")
print("1.Quem desenvolveu o jogo grand theft auto (GTA) ? \n (A) Rockstar game \n (B) Santa Monica Studio \n (C) Activision \n (D) Electronic Arts (EA) \n (E) Riot Games \n")
answer_1 = input("Reposta: ")

if answer_1 == "A":
    print("Corrreto!\n")
    score = score + 1
else:
    print("Incorreto!\n")
    
print("2.Quem desenvolveu o jogo good of war (Bom de guerra) ? \n (A) Rockstar game \n (B) Electronic Arts (EA) \n (C) Santa Monica Studio \n (D) Activision \n (E) Riot Games \n")
answer_2 = input("Reposta: ")

if answer_2 == "C":
    print("Correto!\n")
    score = score + 1
else:
    print("Incorreto\n!")

print("3. Quem desenvolveu a saca call of duty ? \n (A) Rockstar game \n (B) Santa Monica \n (C) Activision \n (D) Electronic Arts (EA) \n (E) Riot Games \n")
answer_3 = input("Reposta: ")

if answer_3 == "C":
    print("Correta!\n")
    score = score + 1
else:
    print("Incorreto!\n")

print("4.Quem desenvolveu a saca Battlefield ? \n (A) Rockstar game \n (B) Eletronic arts (EA) \n (C) Santa Monica \n (D)Activision \n (E) Riot Games \n")
answer_4 = input("Reposta: ")

if answer_4 == "B":
    print("Correto!\n")
    score = score + 1
else:
    print("Incorreto!\n")

print("5.Quem desenvolveu o jogo Legue of legends? \n (A) Rockstar game \n (B) Santa Monica \n (C) Eletronic Arts (EA) \n (D)Activision \n (E) Riot Games \n")
answer_5 = input("Reposta: ")

if answer_5 == "E":
    print("Correto!\n")
    score = score + 1
else:
    print("Incorreto!\n")

print(f"Parabens voce acertou:{score}/5")
print("fim.")