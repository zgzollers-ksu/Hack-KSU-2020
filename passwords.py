import itertools

scraped_words = []
num_words = []
alpha_words = []
sym_words = []

pool = []


def generate_passwords(entropy: int):
    pass


def generate_num_words(max: int, min: int=1):
    characters = [str(num) for num in range(10)]
    words = []

    for i in range(min, max + 1):
        for item in itertools.combinations_with_replacement(characters, i):
            word = ""

            for c in item:
                word = word + c

            words.append(word)

    return words
