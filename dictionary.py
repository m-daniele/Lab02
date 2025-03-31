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

    def translateWordWildCard(self):
        pass

    def printAllWords(self):
        if not self.alien_dict:
            print("Il dizionario è vuoto.")
            return

        for alien_word, translations in self.alien_dict.items():
            print(f"{alien_word} -> {', '.join(translations)}")