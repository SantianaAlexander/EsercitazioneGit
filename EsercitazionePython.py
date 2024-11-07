boolean = True
Risultato = 0
while boolean:
    Num = int(input("Inserisci un numero e premi INVIO: "))
    Risultato = Risultato + Num
    if (Num == 0):
        print("Il risultato è " + str(Risultato))
        break