import requests
from bs4 import BeautifulSoup as bs
from textblob import TextBlob as tb
from nltk.corpus import wordnet

class spider:

    class_nouns = []
    def __init__(self):
        pass

    def make_request(self, url: str):
        page = requests.get(url)

        soup = bs(page.content, 'html.parser')

        blob = tb(str(soup.find_all("p")))

        nouns = []
        for i in blob.noun_phrases:
            if i not in nouns and i.isalnum():
                nouns.append(i)

        synonyms = []
        for i in nouns:
            for syn in wordnet.synsets(i):
                for lm in syn.lemmas():
                    synonyms.append(lm.name())

        nouns = nouns + synonyms
        #print(nouns)

        fixed_nouns = []
        for i in nouns:
            if i not in fixed_nouns:
                fixed_nouns.append(i)

        self.class_nouns = fixed_nouns

