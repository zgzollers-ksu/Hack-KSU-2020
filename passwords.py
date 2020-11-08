import itertools
import string
import hashlib
import math


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
    # alpha_up = generate_words(list(string.ascii_lowercase), 3)
    # alpha_lo = generate_words(list(string.ascii_uppercase), 3)
    alpha_al = generate_words(list(string.ascii_letters), 3)
    scraped = []

    char_pool = []
    char_pool.extend(numeric)
    char_pool.extend(alpha_al)
    passwd_len = entropy_length(entropy, len(char_pool))

    passwords = generate_words(char_pool, passwd_len)

    return {str(hashlib.sha256(bytes(word, 'utf-8')).digest()) : word for word in passwords}


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
        for item in itertools.product(char_set, repeat=i):
            # Assemble characters into a String and append to the list
            word = ""

            for c in item:
                word = word + c

            words.append(word)

    return words


def entropy_length(entropy: float, num_chars: int):
    """
    Calculates the maximum length of a password given the maximum entropy (bits) and number of characters in the
    character pool. If there is a decimal, the value is rounded up to the nearest whole integer.

    :param entropy: maximum bits of entropy
    :param num_chars: number of characters in the character pool
    :return: maximum length of a password
    """

    return round(math.log((2 ** entropy), num_chars))
