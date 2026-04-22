import time

print("=======MENU=========")
print("Seleziona il gioco che vuoi giocare: ")

scelta = ""
while scelta != 3:
    print("1. Gioco dei dadi")
    print("2. Gioco FizzBuzz")
    print("3. Esci")

    scelta = int(input("Scegli il numero del gioco che vuoi giocare: \n"))

    if scelta == 1:
        print("Hai scelto il gioco dei dadi.")
        time.sleep(1)
        print("Caricamento in corso...")
        time.sleep(3)
        import Dadi
    elif scelta == 2:
        print("Hai scelto il gioco FizzBuzz.")
        time.sleep(1)
        print("Caricamento in corso...")
        time.sleep(3)
        import FizzBuzz
    elif scelta == 3:
        print("Grazie, torna a giocare quando vuoi.")
        break
    else:
        print("Digita un numero corretto")
print("Programma terminato")
