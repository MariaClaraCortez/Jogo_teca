import random
numero1 = random.randint(0,20)
numero2 = random.randint(0,20)
resultado = numero1 * numero2
pergunta = int(input(f"Quanto será {numero1} x {numero2}? "))
if pergunta == numero1 * numero2:
    print("Parabéns vc acertou!!")
else:
    print(f"Que pena, você errou, o resultado era {resultado}")
