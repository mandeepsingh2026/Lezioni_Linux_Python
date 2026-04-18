#Es2. Username e password. Chiedi all'utente entrambi se sono user == "admin" e pass == "1234" l'utente può accedere




username = input("Nome utente:")

if username == "admin":
    password = input("Inserire password")
    if password == "1234":
        print("Accesso consentito")
    else:
        print("Accesso negato")
else:
    print("Username errato")
