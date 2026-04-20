password = "abcdef"



# Bloccare un ciclo infinito
contatore = 1

while True:
    print(contatore)
    contatore +=1
    if contatore >= 100:
        break
print("Sono uscito dal while interrompendo lo streatement")
