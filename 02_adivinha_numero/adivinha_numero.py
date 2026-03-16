import random
print('''
______________________________________________________________________
                                                                     
 _____   _ _     _     _                 _____                       
|  _  |_| |_|_ _|_|___| |_ ___    ___   |   | |_ _ _____ ___ ___ ___ 
|     | . | | | | |   |   | -_|  | . |  | | | | | |     | -_|  _| . |
|__|__|___|_|\_/|_|_|_|_|_|___|  |___|  |_|___|___|_|_|_|___|_| |___|
                                                                     
______________________________________________________________________
 ''')
print(''' 
_______________________________________________________________________________________________________________________________
 
      ╔╦╗┌─┐┌┐┌┌┬┐┌─┐  ┌─┐┌┬┐┬┬  ┬┬┌┐┌┬ ┬┌─┐┬─┐  ┌─┐  ┌┐┌┬ ┬┌┬┐┌─┐┬─┐┌─┐  ┌─┐ ┬ ┬┌─┐  ┌─┐┌─┐┌┬┐┌─┐┬ ┬  ┌─┐┌─┐┌┐┌┌─┐┌─┐┌┐┌┌┬┐┌─┐
       ║ ├┤ │││ │ ├┤   ├─┤ │││└┐┌┘││││├─┤├─┤├┬┘  │ │  ││││ ││││├┤ ├┬┘│ │  │─┼┐│ │├┤   ├┤ └─┐ │ │ ││ │  ├─┘├┤ │││└─┐├─┤│││ │││ │
       ╩ └─┘┘└┘ ┴ └─┘  ┴ ┴─┴┘┴ └┘ ┴┘└┘┴ ┴┴ ┴┴└─  └─┘  ┘└┘└─┘┴ ┴└─┘┴└─└─┘  └─┘└└─┘└─┘  └─┘└─┘ ┴ └─┘└─┘  ┴  └─┘┘└┘└─┘┴ ┴┘└┘─┴┘└─┘
_______________________________________________________________________________________________________________________________
''')
print('''
____________________________________________________
┏━╸┏━┓┏━╸┏━┓╻  ╻ ╻┏━┓   ╻ ╻┏┳┓   ┏┓╻╻╻ ╻┏━╸╻   
┣╸ ┗━┓┃  ┃ ┃┃  ┣━┫┣━┫   ┃ ┃┃┃┃   ┃┗┫┃┃┏┛┣╸ ┃  ╹
┗━╸┗━┛┗━╸┗━┛┗━╸╹ ╹╹ ╹   ┗━┛╹ ╹   ╹ ╹╹┗┛ ┗━╸┗━╸╹
      Nivel Facil: (1 a 10)
      Nivel Medio: (1 a 20)
      Nivel Dificil: (1 a 50)
      Nivel SENAI: (1 a 200)
____________________________________________________

''')
nivel = int(input("Qual será seu Nivel?"))
numero_perguntado = int(input("Qual será sua tentativa?"))

if nivel == 1:
    numero_aleatorio = random.randint(0,10)
    if numero_perguntado == numero_aleatorio:
        print("Muito bem, você acertou!!")
    else :
        print(f"Que pena, você errou! Eu estava pensando no número {numero_aleatorio}")

if nivel == 2:
    numero_aleatorio = random.randint(0,20)
    if numero_perguntado == numero_aleatorio:
        print("Muito bem, você acertou!!")
    else :
        print(f"Que pena, você errou! Eu estava pensando no número {numero_aleatorio}")

if nivel == 3:
    numero_aleatorio = random.randint(0,50)
    if numero_perguntado == numero_aleatorio:
        print("Muito bem, você acertou!!")
    else :
        print(f"Que pena, você errou! Eu estava pensando no número {numero_aleatorio}")

if nivel == 4:
    numero_aleatorio = random.randint(0,200)
    if numero_perguntado == numero_aleatorio:
        print("Muito bem, você acertou!!")
    else :
        print(f"Que pena, você errou! Eu estava pensando no número {numero_aleatorio}")
if nivel >4 :
    print("Sinto muito, não temos esse nivel")
if nivel <1 :
    print("Sinto muito, não temos esse nivel")