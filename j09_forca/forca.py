import os
import random

def limpar_tela():
    os.system("cls")

def escolher_palavra() -> str:
    palavras = ["BROCOLIS","LARANJA","TRIANGULO","REMEDIO","MORCEGO","ACEROLA", "BICICLETA"]
    palavra_aleatoria = random.choice(palavras)

    return palavra_aleatoria

limpar_tela()

def desenhar_forca(erro):
    if erro == 0:
        print("""
            _ _ _ _ _
            |       |
            |
            |
            |
            |
            |
            |
            """)
    elif erro == 1:
        print("""
            _ _ _ _ _
            |       |
            |     (° °)
            |
            |
            |
            |
            |
            """)
        limpar_tela()

    elif erro == 2:
        print("""
            _ _ _ _ _
            |       |
            |     (° °)
            |       |
            |       |
            |       
            |
            |
            |
            """)
        

    elif erro == 3:
        print("""
            _ _ _ _ _
            |       |
            |     (° °)
            |      _|
            |       |
            |       
            |
            |
            |
            """)
        

    elif erro == 4:
        print("""
            _ _ _ _ _
            |       |
            |     (° °)
            |      _|_
            |       |
            |       
            |
            |
            |
            """)
        

        
    elif erro == 5:
        print("""
            _ _ _ _ _
            |       |
            |     (° °)
            |      _|_
            |       |
            |      /
            |
            |
            |
            """)
        

    elif erro == 6:
        print(r"""
            _ _ _ _ _
            |       |
            |     (° °)
            |      _|_
            |       |
            |      / \
            |
            |
            |
            """)


    
