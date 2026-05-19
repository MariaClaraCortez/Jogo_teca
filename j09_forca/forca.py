import os
import random

def limpar_tela():
    os.system("cls")

def escolher_palavra() -> str:
    palavras = ["BROCOLIS","LARANJA","TRIANGULO","REMEDIO","MORCEGO","ACEROLA", "BICICLETA"]
    palavra_aleatoria = random.choice(palavras).upper()

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
            |      😰
            |
            |
            |
            |
            |
            |
            """)
        

    elif erro == 2:
        print("""
            _ _ _ _ _
            |       |
            |      😰
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
            |      😰
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
            |      😰
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
            |      😰
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
        contador = 0
        escolha = escolher_palavra()
        lista_tracos = gerar_tracos(escolha)
        lista_tentativas = []
        
        
        while True:
            limpar_tela()

            desenhar_forca(contador)

            print("              ",*lista_tracos)
            print("Suas tentivas foram: ",*lista_tentativas)

            if "_" not in lista_tracos:
                print("Você ganhou!!🥳🥳")
                break

            letra = perguntar_letra()

            if letra not in escolha:
                contador += 1
                lista_tentativas.append(letra)
            if contador >= 6:
                print("Você Perdeu👎")
                print(f"A palavra era: {escolha}")
                break
            if letra in escolha:
                contador_lista = 0
                for lp in escolha:
                    if lp == letra:
                        lista_tracos[contador_lista] = letra
                    contador_lista += 1
            






if __name__ == "__main__":
    jogar_forca()