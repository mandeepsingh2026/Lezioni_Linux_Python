# 1 Stampa i numeri da 1 al numero >100 scelto dall'utente. I multipli di 3 deve uscire "Buzz" e per i multipli di 5 "Fizz". Per i numeri multipli sia di 3 che di 5 "BuzzFizz".
def avvia_FizzBuzz():
    continua = True

    while continua:
        print("\nBenvenuto in FizzBuzz")

        numero = int(input("Seleziona un numero maggiore di 100: "))

        while numero <= 100:
            numero = int(input("Seleziona un numero maggiore di 100!"))

        for i in range(1, numero + 1):
            if i % 3 == 0 and i % 5 == 0:
                print("FizzBuzz")
            elif i % 3 == 0:
                print("Fizz")
            elif i % 5 == 0:
                print("Buzz")
            else:
                print(i)

        risposta = input("Vuoi rigiocare a FizzBuzz? (si/no): ").lower()

        if risposta == "no":
            continua = False
            print("Grazie per aver giocato. Torno al menu...")

avvia_FizzBuzz()