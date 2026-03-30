import random

print('''
######################################################
    ,---.               
    |    ,---.,---.,---.
    |    ,---||   |`---.
    `---'`---^`---'`---'
 ##########################
                     
    |__)_ _  _ _  _ 
    | \(-(_)| (_|_) 
         _/          
      

- Vômito vence Meia e Lixo
- Meia vence Peido
- Peido vence Vômito
-🗑️ Lixo vence tudo (menos Vômito)
###################################################
      ''')


jogador = input("Escolha entre vomito, peido, meia ou lixo: ").lower()
computador = random.choice(["vomito", "peido", "meia", "lixo"])

print(f"Você: {jogador}")
print(f"Computador: {computador}")
  
if jogador == computador:
    print("Empate!")

elif jogador == "vomito" and computador == "meia":
    print("Parabéns, você ganhou!")
elif jogador == "meia" and computador == "peido":
    print("Parabéns, você ganhou!")
elif jogador == "peido" and computador == "vomito":
    print("Parabéns, você ganhou!")

elif jogador == "lixo":
    if computador == "vomito":
        print("Você perdeu HAHAHA")
    else:
        print("Parabéns, você ganhou!")

elif computador == "lixo":
    if jogador == "vomito":
        print("Parabéns, você ganhou!")
    else:
        print("Você perdeu HAHAHA")

else:
    print("Você perdeu HAHAHA")

