# 1 Stampa i numeri da 1 al numero >100 scelto dall'utente. I multipli di 3 deve uscire "Buzz" e per i multipli di 5 "Fizz". Per i numeri multipli sia di 3 che di 5 "BuzzFizz".

numero = int(input("Scegli un numero maggiore di 100: "))

while numero < 100:
    print("Numero troppo piccolo, riscrivi un numero: ")
    numero = int(input("Scrivi un numero maggiore di 100: "))

for i in range(1, numero +1):
    if i % 3 == 0 and i % 5 == 0:
        print("BuzzFizz")
    elif i % 3 == 0:
        print("Buzz")
    elif i % 5 == 0:
        print("Fizz")
    else:
        print(i)