import random

def jogar_adivinha_numero():

    print('''
    ______________________________________________________________________
                                                                        
    _____   _ _     _     _                 _____                       
    |  _  |_| |_|_ _|_|___| |_ ___    ___   |   | |_ _ _____ ___ ___ ___ 
    |     | . | | | | |   |   | -_|  | . |  | | | | | |     | -_|  _| . |
    |__|__|___|_|\_/|_|_|_|_|_|___|  |___|  |_|___|___|_|_|_|___|_| |___|
                                                                        
    ______________________________________________________________________
    ''')
    print(''' 
    _____________________________________________________________________________________________________________________
    
    ___ ____ _  _ ___ ____    ____ ___  _ _  _ _ _  _ _  _ ____ ____    ____    _  _ _  _ ____ ____ ____    
     |  |___ |\ |  |  |___    |__| |  \ | |  | | |\ | |__| |__| |__/    |  |    |\ | |\/| |___ |__/ |  |    
     |  |___ | \|  |  |___    |  | |__/ |  \/  | | \| |  | |  | |  \    |__|    | \| |  | |___ |  \ |__|    


        ____ _  _ ____    ____ ____ ___ ____ _  _    ___  ____ _  _ ____ ____ _  _ ___  ____ 
        |  | |  | |___    |___ [__   |  |  | |  |    |__] |___ |\ | [__  |__| |\ | |  \ |  | 
        |_\| |__| |___    |___ ___]  |  |__| |__|    |    |___ | \| ___] |  | | \| |__/ |__| 
       
    _____________________________________________________________________________________________________________________
    ''')
    print('''
    ____________________________________________________
    ____ ____ ____ ____ _    _  _ ____    _  _  _ _  _    _  _ _  _ ____ _    
    |___ [__  |    |  | |    |__| |__|    |  |  | |\/|    |\ | |  | |___ |    
    |___ ___] |___ |__| |___ |  | |  |    |__| _| |  |    | \|  \/  |___ |___ 
                                                                          
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