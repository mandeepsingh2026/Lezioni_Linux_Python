import random
import time

def avvia_Dadi():
    continua = True
    while continua:
    
        print("Benvenuto al gioco dei dadi.")
        time.sleep(2)
        print("Se escono due numeri uguali vinci!")
        time.sleep(3)

        comando=input("Scrivi - Lancia - per lanciare i dadi: ").lower()
        while comando != "lancia":
            print("Hai scritto male, riprova.")
            comando= input("Scrivi - Lancia - per lanciare i dadi.").lower()

        dado1 = random.randint(1,6)
        dado2 = random.randint(1,6)

        print("I dadi sono stati lanciati...")
        
        time.sleep(3)

        print("Sono usciti", dado1 ,"e" ,dado2 )
        time.sleep(2)

        if dado1 == dado2:
            print("Hai vinto!!")
        else:
            print("Ritenta, sarai piu fortunato.")
            
        risposta = input("Vuoi riprovare? (si/no): ").lower()
            
        if risposta == "no":
             continua = False
             time.sleep(1)
             print("Grazie per aver giocato, a presto!")
        else:
            print("Sono usciti", dado1, "e", dado2)




avvia_Dadi()
