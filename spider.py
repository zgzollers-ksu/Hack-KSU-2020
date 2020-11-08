import requests
from bs4 import BeautifulSoup as bs
from textblob import TextBlob as tb
from nltk.corpus import wordnet

class spider:

    class_nouns = []
    def __init__(self):
        pass

    def make_request(self, url: str):
        #send get request for html to the given url
        page = requests.get(url)

        #parse the html using BeautifulSoup
        soup = bs(page.content, 'html.parser')

        #use BeautifulSoup to find all paragraph tags,
        #convert that to a string, and send it to a TextBlob object
        blob = tb(str(soup.find_all("p")))

        nouns = []
        for i in blob.noun_phrases:
            #append every alphanumeric noun in the html to a list
            if i not in nouns and i.isalnum():
                nouns.append(i)

        synonyms = []
        #for every noun we've collected...
        for i in nouns:
            #for every set of each synonym (sets also contain part of speech) of that noun...
            for syn in wordnet.synsets(i):
                #and for every synonum (ignore part of speach)
                for lm in syn.lemmas():
                    #append to another list
                    synonyms.append(lm.name())

        #add those two lists together
        nouns = nouns + synonyms

        fixed_nouns = []
        #iterate over into a new list, ignoring repeats
        for i in nouns:
            if i not in fixed_nouns:
                fixed_nouns.append(i)

        self.class_nouns = fixed_nouns