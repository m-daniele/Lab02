import translator as tr

t = tr.Translator()
t.loadDictionary("dictionary.txt")  # Load dictionary only once at start

while(True):

    t.printMenu()

    try:
        txtIn = input("Inserisci la tua scelta: ")
        choice = int(txtIn)
        # Add input control here!

        if choice == 1:
            print("\nAggiungi nuova parola (formato: <parola aliena> <traduzione>)")
            entry = input()
            t.handleAdd(entry)

        elif choice == 2:
            print("\nCerca una traduzione (inserisci la parola aliena)")
            query = input()
            t.handleTranslate(query)

        elif choice == 3:
            print("\nDizionario completo:\n")
            t.dictionary.printAllWords()

        elif int(txtIn) == 4:
            print("Grazie e arrivederci!")
            break
        else:
            print("Scelta non valida. Inserisci un numero tra 1 e 4.")
    except ValueError:
        print("Input non valido. Inserisci un numero tra 1 e 4.")