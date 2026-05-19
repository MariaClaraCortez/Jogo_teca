
from j01_madf_libs.Historinha1 import jogar_historinha
from j02_adivinha_numero.adivinha_numero import jogar_adivinha_numero
from j03_tabuada.jogo_da_tabuada import jogar_tabuada
from j04_par_ou_impar.par_ou_impar import jogar_par_ou_impar
from j05_qual_vc_escolhe.caos import jogar_caos
from j06_cara_coroa.cara_ou_coroa import jogar_cara_ou_coroa
from j07_adivinha.adivinha import jogar_adivinha
from j08_genius.genius import jogar_genius
from j09_forca.forca import jogar_forca
print("""
          )             )                               
       ( /(  (       ( /(     *   )        (     (      
   (   )\()) )\ )    )\())  ` )  /( (      )\    )\     
   )\ ((_)\ (()/(   ((_)\    ( )(_)))\   (((_)((((_)(   
  ((_)  ((_) /(_))_   ((_)  (_(_())((_)  )\___ )\ _ )\  
 _ | | / _ \(_)) __| / _ \  |_   _|| __|((/ __|(_)_\(_) 
| || || (_) | | (_ || (_) |   | |  | _|  | (__  / _ \   
 \__/  \___/   \___| \___/    |_|  |___|  \___|/_/ \_\  
      
      POR: Maria Clara Cortez Dias
                                                        
""")
while True:
    print("""
    ************************************
          0 = SAIR
          01 = HISTÓRINHA
          02 = ADIVINHA O NÚMERO
          03 = TABUADA
          04 = PAR OU IMPAR
          05 = CAOS
          06 = CARA OU COROA
          07 = ADIVINHA O NÚMERO 2
          08 = GENIUS
          09 = FORCA

    ***********************************
    """)
    jogo = int(input("Qual jogo você quer jogar???"))
    if jogo == 1:
        jogar_historinha()
    elif jogo == 2:
        jogar_adivinha_numero()
    elif jogo == 3:
        jogar_tabuada()
    elif jogo == 4:
        jogar_par_ou_impar()
    elif jogo == 5:
        jogar_caos()
    elif jogo == 6:
        jogar_cara_ou_coroa()
    elif jogo == 7:
        jogar_adivinha()
    elif jogo == 8:
        jogar_genius()
    elif jogo == 9:
        jogar_forca()
    elif jogo == 0:
        print("Foi ótimo jogar com você")
        break
    