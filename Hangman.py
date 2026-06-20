import random
words = [
  "synecdoche", "queueing", "xylophone", "knight", "czar",
  "onomatopoeia", "juxtaposition", "psoriasis", "mnemosyne", "sphinx",
  "pterodactyl", "schizophrenia", "quixotic", "zeugma", "glyph",
  "isthmus", "apocalypse", "rhythmless", "counterintuitive", "hippopotomonstrosesquipedaliophobia",
  "euonym", "kaleidoscope", "thoroughbred", "sesquipedalian", "anemone",
  "phthisis", "eisteddfod", "debt", "subtle", "hors d'oeuvre",
  "pneumonoultramicroscopicsilicovolcanoconiosis",
  "myrrh", "crypt", "cwm", "crwth", "psst",
  "tsunami", "bdellium", "ptolemaic", "tmesis", "zanyism",
  "schtschurowskia", "xenotransplantation", "hexylresorcinol", "quizzicality",
  "knaidel", "sforzando", "tzimmes", "chutzpah", "fjord",
  "whiskey", "eczema", "djinn", "ngwee", "squirrel",
  "strengths", "twelfths", "sixths", "brougham", "lymph"
]
final_word = random.choice(words)
display = ["_"] * len(final_word)
print(" ".join(display))
lives = 6

HANGMANPICS = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
      |
      |
      |
      |
=========''']

guessed = []
while display != list(final_word) and lives > 0:
    guess = input("Enter a letter: ").lower()

    if guess in final_word:
        for i in range(len(final_word)):
            if final_word[i] == guess:
                display[i] = guess
        print(HANGMANPICS[lives])        
        guessed.append(guess)
    else:
        lives -= 1
        print(HANGMANPICS[lives])
        guessed.append(guess)
    print(" ".join(display))
    print("Guessed letters:")
    print(" , ".join(guessed))
if lives == 0:
    print("You lost! The word was:", final_word)
else:
    print("You won! 🎉")