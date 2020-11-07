import hashlib

def find_match(options: dict, hash: list):
    for item in hash:
        if item in dict.keys():
            return dict[item]

    return "\0"

