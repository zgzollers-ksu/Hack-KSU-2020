import itertools
import string
import hashlib


def generate_passwords(entropy: float, max_num: int = -1, ):
    """
    Generate all possible passwords with the defined character set from a minimum to n (inclusive) bits of entropy or a
    maximum number of items (whichever comes first). If a password of length 1 exceeds the maximum entropy given the
    character set, then an empty list will be returned (the character set will not be adjusted).

    :param entropy: Maximum password entropy using the given character/word set
    :param max_num: Maximum number of passwords to be generated. Useful for generating partial sets of passwords given
        a high entropy value.
    :return: An exhaustive List of passwords meeting the requirements of entropy, length, and character set
    """

    numeric = generate_words(list(string.digits), 3)
    alpha_up = generate_words(list(string.ascii_lowercase), 3)
    alpha_lo = generate_words(list(string.ascii_uppercase), 3)
    alpha_al = generate_words(list(string.ascii_letters), 3)
    scraped = []

    char_pool = numeric + alpha_up + alpha_lo + alpha_al + scraped
    passwd_len = entropy_length(entropy, len(char_pool))

    passwords = generate_words(char_pool, passwd_len)

    return [{hashlib.sha256(word), word} for word in passwords]



def generate_words(char_set: list, max: int, min: int=1):
    """
    Generate all possible combinations of characters between a minimum (inclusive) and maximum (inclusive) word
    length.

    :param char_set: all possible characters to be included in generated words
    :param max: maximum number of characters in a word
    :param min: minimum number of characters in a word
    :return: list of words containing all possible combinations of characters in the provided character set
    """

    words = []

    # For each length between the minimum and maximum (inclusive)
    for i in range(min, max + 1):
        # For each combination of length i
        for item in itertools.permutations(char_set, i):
            # Assemble characters into a String and append to the list
            word = ""

            for c in item:
                word = word + c

            words.append(word)

    return words


def entropy_length(entropy: float, num_chars: int):
    pass
