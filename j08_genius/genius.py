import os
import time
import random
def jogar_genius():
    dicionario_cores = {"VERMELHO": "C0",
                        "AZUL": "90",
                        "AMARELO": "60",
                        "VERDE": "20",
                        "LILAS": "D0"}



    lista_cores = ["VERDE", "AZUL", "AMARELO", "VERMELHO", "LILAS"]
    lista_sequencia = []


    def limpar_tela():
        os.system("color 07")
        os.system("cls")


    def mudar_cor(cor):
        codigo_cor = dicionario_cores[cor]
        os.system(f"color {codigo_cor}")
        time.sleep(1)
        limpar_tela()


    print("""
    *********************************************************************************************************
    ____ ____  _ ____    ___  ____ _  _    _  _ _ _  _ ___  ____    ____ ____    ____ ____ _  _ _ _  _ ____ 
    [__  |___  | |__|    |__] |___ |\/|    |  | | |\ | |  \ |  |    |__| |  |    | __ |___ |\ | | |  | [__  
    ___] |___ _| |  |    |__] |___ |  |     \/  | | \| |__/ |__|    |  | |__|    |__] |___ | \| | |__| ___] 
        
                                        REPITA AS CORES SEM ERRAR
    *********************************************************************************************************                                                                                                        
    """)

    input("Pressione ENTER para começar...")
    limpar_tela()

    while True:
        cor_aleatoria = random.choice(lista_cores)
        lista_sequencia.append(cor_aleatoria)
        for cor_lista in lista_sequencia:
            mudar_cor(cor_lista)

        print("""
                V - VERDE
                A - AZUL
                M - AMARELO
                R - VERMELHO
                L - LILAS
        """)

        resposta = input("Digite a sequência correta: ").upper()
        dicionario_resposta = {"V": "VERDE",
                            "A": "AZUL",
                            "M": "AMARELO",
                            "R": "VERMELHO",
                            "L": "LILAS"}
        

        lista_resposta = []
        for letra in resposta:
            cor = dicionario_resposta.get(letra)
            lista_resposta.append(cor)

        if lista_resposta != lista_sequencia:
            print("Você errou!")
            print("A sequencia era:")
            print(*lista_sequencia)
            break
        else:
            print("Você acoertou")
            print("Vamos para a próxima fase ")
            input("Aperte ENTER quando estiver pronto ")
            limpar_tela()





