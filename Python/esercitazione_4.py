#Es. Gioco dei dadi. Lancia 2 dadi (numero casuale tra 1 e un numero scelto dall'utente. Faccio scegliere all'utente il numero di facce del dado). Se i due numeri sono uguali l'utente vince, altrimenti perde.

import random
facce_dado = int(input("quante facce ha il dado?"))

dado1 = random.randint(1,facce_dado)
dado2 = random.randint(1,facce_dado)

print("Sono usciti:", dado1 ,("e"), dado2)

if dado1 == dado2:
    print("Hai vinto!")
else:
    print("hai perso!")