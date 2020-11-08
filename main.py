import hashlib
import passwords


def find_match(options: dict, hash: list):
    for item in hash:
        if item in dict.keys():
            return dict[item]

    return "\0"

passwords.generate_passwords(1)