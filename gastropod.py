
import json
import random

def load_words():
    with open('words_dict.json') as f:
        data = json.load(f)
    return data

def randomWordFromFile(wordbank):
    r = random.choice(list(wordbank.items()))
    key, value = r
    return key


if __name__ == '__main__':
    english_words = load_words()
    slug = ""
    for i in range(0, 3):
        word = (randomWordFromFile(english_words))
        slug = slug + (word + ".") if not i == 2 else slug + word

    print(slug) 