class Dictionary:
    def __init__(self):
        self.alien_dict = {}

    def addWord(self,alien_word, translation):
        if alien_word in self.alien_dict:
            if translation not in self.alien_dict[alien_word]:
                self.alien_dict[alien_word].append(translation)
        else:
            # aggiungi la parola aliena e la traduzione al dizionario
            self.alien_dict[alien_word] = [translation]
        return True

    def translate(self, alien_word):
        return self.alien_dict.get(alien_word, None)

    def translateWordWildCard(self, query_with_wildcard):
        # Gestiamo la ricerca con wildcard
        matches = {}

        # Troviamo la posizione del carattere wildcard
        wildcard_pos = query_with_wildcard.find('?')

        # Creiamo due parti della stringa: parte prima e dopo del wildcard
        prefix = query_with_wildcard[:wildcard_pos]
        suffix = query_with_wildcard[wildcard_pos + 1:]

        # Controlliamo tutte le parole nel dizionario
        for word in self.alien_dict:
            # Verifichiamo che la lunghezza sia uguale
            if len(word) == len(query_with_wildcard):
                # Verifichiamo che il prefisso e il suffisso corrispondano
                if (word.startswith(prefix) and word.endswith(suffix) and
                        len(prefix) + len(suffix) + 1 == len(word)):
                    matches[word] = self.alien_dict[word]
        return matches

    def printAllWords(self):
        if not self.alien_dict:
            print("Il dizionario è vuoto.")
            return

        for alien_word, translations in self.alien_dict.items():
            print(f"{alien_word} -> {', '.join(translations)}")