passwords = {}
words = ["Hello", "birds"]
words2 = []

def generate_passwords(words):
    for i in range(len(words)):
        words2.append(words[i])
        add_numbers(words[i], words2)

def add_numbers(word, words2):
    for x in range(1, 100):
        words2.append("{}{}".format(word, x))

#def hash_passwords():