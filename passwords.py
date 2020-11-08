import itertools

scraped_words = []
num_words = []
alpha_words = []
sym_words = []

pool = []


def generate_passwords(entropy: int, max_num: int = -1):
    """
    Generate all possible passwords with the defined character set from 1 to n (inclusive) bits of entropy or a maximum
    number of items (whichever comes first).

    :param entropy: Maximum password entropy using the given character/word set
    :param max_num: Maximum number of passwords to be generated. Useful for generating partial sets of passwords given
        a high entropy value.
    :return: An exhaustive List of passwords meeting the requirements of entropy, length, and character set
    """

    pass


def generate_num_words(max: int, min: int=1):
    """
    Generate all possible combinations of numeric characters between a minimum (inclusive) and maximum (inclusive) word
    length.

    :param max: maximum number of characters in a word
    :param min: minimum number of characters in a word
    :return: list of words containing all possible combinations of numeric characters
    """

    characters = [str(num) for num in range(10)]  # list of numeric characters (0 - 9)
    words = []

    # For each length between the minimum and maximum (inclusive)
    for i in range(min, max + 1):
        # For each combination of length i
        for item in itertools.combinations_with_replacement(characters, i):
            # Assemble characters into a String and append to the list
            word = ""

            for c in item:
                word = word + c

            words.append(word)

    return words
