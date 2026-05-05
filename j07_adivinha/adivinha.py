import random
def jogar_adivinha():
    contador = 0
    numero_aleatorio = random.randint(0,100)
    while True:
        numero_perguntado = int(input("Qual será sua tentativa?"))
        if numero_aleatorio == numero_perguntado:
            print("Muito bem, você acertou!!")
            break
        elif numero_perguntado < numero_aleatorio:
            print("O número que estou pensando é maior")
        elif numero_perguntado > numero_aleatorio:
            print("O número que estou pensando é menor")
        contador = contador + 1
        if contador == 5:
            print(f"Suas chances acabaram! Eu estava pensando no número {numero_aleatorio}")
            break

