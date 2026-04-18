#Es3. Dato un certo numero verifica se si trova tra 20 e 100 oppure se si trova tra 50 e 200


numero = int(input("Inserisci un numero:"))

if (numero >= 50 and numero <=100):
    print("Il numero si trova tra 50 e 100")
elif numero >=20 and numero < 50 :
    print ("il numero si trova tra 20 e 50")
elif (numero >100 and numero <= 200):
    print ("il numero si trova tra 100 e 200")
else:
    print("il numero non si trova tra 50 e 100")