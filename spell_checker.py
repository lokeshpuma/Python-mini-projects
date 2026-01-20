from spellchecker import SpellChecker

class SpellCheckerApp:
    def __init__(self, language='en'):
        self.spell = SpellChecker(language=language)

    def check_spelling(self, text):
        words = text.split()
        corrected_words = []

        for word in words:
            corrected_word = self.spell.correction(word)

            if corrected_word != word:
                print(f"Correcting '{word}' → '{corrected_word}'")

            corrected_words.append(corrected_word)

        return ' '.join(corrected_words)

    def run(self):
        print("Welcome to the Spell Checker!")

        while True:
            text = input("Enter text to check spelling (or type 'exit' to quit): ")
            if text.lower() == 'exit':
                print("Exiting the Spell Checker. Goodbye!")
                break

            corrected_text = self.check_spelling(text)
            print(f"Corrected Text: {corrected_text}")

if __name__ == "__main__":
    app = SpellCheckerApp()
    app.run()