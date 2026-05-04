
import random

def jogar_cara_ou_coroa():


    print('''

            _.-'~~`~~'-._
        .'`  B   E   R  `'.
        / I               T \
    /`       .-'~"-.       `\
    ; L      / `-    \      Y ;
    ;        />  `.  -.|        ;
    |       /_     '-.__)       |
    |        |-  _.' \ |        |
    ;        `~~;     \\        ;
    ;  INGODWE /      \\)P    ;
    \  TRUST '.___.-'`"     /
    `\                   /`
        '._   1 9 9 7   _.'
    jgs    `'-..,,,..-'`

    ''')

    escolha= input("Você quer cara ou coroa?").lower()
    computador = random.choice(["cara","coroa"])

    if escolha == computador:
        print(f"Parabéns, você ganhou!!O sorteado foi {computador}")
    else:
        print(f"Que pena, você perdeu!! O sorteado foi {computador}")

