eta = int(input("Quanti anni hai?"))

giorno = input("oggi è:").lower()


if eta < 18:
    print("paghi solo 6$")
else:
    if giorno == "sabato" or giorno == "domenica":
        print("paghi 12$")
    else:
        print("oggi paghi 10$")