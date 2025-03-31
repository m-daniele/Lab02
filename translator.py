import dictionary


class Translator:

    def __init__(self):
        self.dictionary = dictionary.Dictionary()

    def printMenu(self):
        # 1. Aggiungi nuova parola
        # 2. Cerca una traduzione
        # 3. Cerca con wildcard
        # 4. Exit
        print("------------------")
        print("Translator Alien-Italian")
        print("------------------")
        print("1. Aggiungi nuova parola")
        print("2. Cerca una traduzione")
        print("3. Stampa tutto il dizionario")
        print("4. Exit")
        print("------------------")
        print()

    def loadDictionary(self, dict):
        try:
            self.dictionary.alien_dict.clear()  # Clear existing dictionary
            with open(dict, "r") as infile:
                for line in infile:
                    parts = line.strip().split(' ', 1)
                    if len(parts) == 2:
                        alien_word = parts[0].lower()
                        translations = parts[1].lower().split()
                        for translation in translations:
                            self.dictionary.addWord(alien_word, translation)
        except FileNotFoundError:
            print(f"File {dict} not found")

    def handleAdd(self, entry):
        # entry is a tuple <parola_aliena> <traduzione1 traduzione2 ...>
        # Verifica che l'input rispetti il formato <parola aliena> <traduzione>
        parts = entry.split(' ', 1)
        if len(parts) != 2:
            print("Formato non valido. Usa: <parola aliena> <traduzione>")
            return False

        alien_word = parts[0].strip().lower()
        translation_text = parts[1].strip().lower()
        translations = translation_text.split()

        # Verifica che siano solo lettere
        if not alien_word.isalpha() or not all(t.isalpha() for t in translations):
            print("Formato non valido. Usa solo lettere.")
            return False

        # Flag per tenere traccia se almeno una traduzione è stata aggiunta
        added = False
        # Aggiungi ogni traduzione al dizionario
        for translation in translations:
            self.dictionary.addWord(alien_word, translation)
            added = True

        if added:
            print(f"Parola aggiunta: {alien_word} -> {' '.join(translations)}")
            # Rewrite the entire dictionary file
            with open("dictionary.txt", "w") as file:
                for aword, trans in self.dictionary.alien_dict.items():
                    file.write(f"{aword} {' '.join(trans)}\n")
        return added


    def handleTranslate(self, query):
        # query is a string <parola_aliena>
        query = query.strip().lower()
        # verifica che siano solo lettere
        if not query.isalpha():
            print("Formato non valido. Usa solo lettere.")
            return False
        # cerca la traduzione
        translations = self.dictionary.translate(query)
        if translations:
            print(f"Traduzioni per: '{query}' -> {', '.join(translations)}")
        else:
            print(f"Parola '{query}' non trovata nel dizionario.")
        pass

    def handleWildCard(self,query):
        # query is a string with a ? --> <par?la_aliena>
        pass

