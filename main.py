import hashlib
import passwords


def find_match(options: dict, hash: list):
    for item in hash:
        if item in dict.keys():
            return dict[item]

    return "\0"

print(passwords.generate_passwords(20, 1000000))