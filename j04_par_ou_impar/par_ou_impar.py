import random
def jogar_par_ou_impar():

    print("""
                                                                                        
        |                   ,---.                            |                    
        |,---.,---.,---.    |---',---.,---.    ,---..   .    |,-.-.,---.,---.,---.
        ||   ||   ||   |    |    ,---||        |   ||   |    || | ||   |,---||    
    `---'`---'`---|`---'    `    `---^`        `---'`---'    `` ' '|---'`---^`    
            `---'                                                |              

        """)

    lado = input("Impar ou Par?").upper()
    if lado == "IMPAR":
        print("Então eu sou o par")
    elif lado == "PAR":
        print("Então eu sou o impar")
    elif lado != "IMPAR" or lado !='PAR':
        print("Não temos essa opção")
        exit()

    numero1 = int(input("Qual será o número de 0 a 10 escolhido?"))
    numero2 = random.randint(0,10)

    if numero1 >10 or numero1 <0:
        print("Você nâo tem esse tanto de dedos")
    else:
        if lado == 'IMPAR':
            resultado= numero1 + numero2
            print(f"{numero1} + {numero2}")
            if resultado % 2 == 1:
                print(f"Parebens vc ganhou, o {resultado} é impar")
            else:
                print(f"Você perdeu, o {resultado} é par")

        if lado == 'PAR':
            resultado= numero1 + numero2
            print(f"{numero1} + {numero2}")
            if resultado % 2 == 0:
                print(f"Parebens vc ganhou, o {resultado} é par")
            else:
                print(f"Você perdeu, o {resultado} é impar")