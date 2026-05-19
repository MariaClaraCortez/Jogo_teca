import os
import random

def limpar_tela():
    os.system("cls")

def escolher_palavra() -> str:
    palavras = ["BROCOLIS","LARANJA","TRIANGULO","REMEDIO","MORCEGO","ACEROLA", "BICICLETA"]
    palavra_aleatoria = random.choice(palavras)

    return palavra_aleatoria

limpar_tela()

def desenhar_forca(erro:int):
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
            |
            """)
    elif erro == 1:
        print("""
            _ _ _ _ _
            |       |
            |    (⊙_◎)
            |
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
            |    (⊙_◎)
            |       |
            |       |
            |       
            |
            |
            |
            |
            """)
        

    elif erro == 3:
        print("""
            _ _ _ _ _
            |       |
            |    (⊙_◎)
            |      _|
            |       |
            |       
            |
            |
            |
            |
            """)
        

    elif erro == 4:
        print("""
            _ _ _ _ _
            |       |
            |    (⊙_◎)
            |      _|_
            |       |
            |       
            |
            |
            |
            |
            """)
        

        
    elif erro == 5:
        print("""
            _ _ _ _ _
            |       |
            |    (⊙_◎)
            |      _|_
            |       |
            |      /
            |
            |
            |
            |
            """)
        

    elif erro == 6:
        print(r"""
            _ _ _ _ _
            |       |
            |      💀
            |      _|_
            |       |
            |      / \
            |
            |
            |
            |
            """)

def gerar_tracos (palavra:str) -> list:
    """gera e retorna uma lisa contendo _ na mesma quantidade que as palavras"""
    quantidade_de_letras = len(palavra)
    tracos = []
    while len(tracos)< quantidade_de_letras:
        tracos.append("_")
    return tracos

#lista_tracos = gerar_tracos("casa")
#print(*lista_tracos)

def perguntar_letra() ->str:
    resposta = input("Me de uma letra ").upper()
    while len(resposta) != 1:
        resposta = input("Eu disse apenas UMA letra: ").upper()
    return resposta

#letra = perguntar_letra()
#print(letra)


def jogar_forca():
        print(r"""
        _____   ___   ____      __   ____ 
        |     | /   \ |    \    /  ] /    |
        |   __||     ||  D  )  /  / |  o  |
        |  |_  |  O  ||    /  /  /  |     |
        |   _] |     ||    \ /   \_ |  _  |
        |  |   |     ||  .  \\     ||  |  |
        |__|    \___/ |__|\_| \____||__|__|                      
        """)

        input("aperte ENTER para começar... ")
        while True:
            limpar_tela()
            contador = 0

            desenhar_forca(contador)

            escolha = escolher_palavra()

            lista_tracos = gerar_tracos(escolha)
            print("              ",*lista_tracos)

            letra = perguntar_letra()

            if letra not in escolha:
                contador += 1



if __name__ == "__main__":
    jogar_forca()