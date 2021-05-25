from app.words import STOP_WORDS, SKIP_WORDS
import re
import unicodedata

def normalize(question):
    question = unicodedata.normalize('NFKC', question) # remplacement des caractères spéciaux
    normalize_question = ''
    fordib_words = STOP_WORDS.union(SKIP_WORDS)
    for word in re.split('\W+', question.lower()):
        if word and word not in fordib_words:
            normalize_question += word + ' '
    return normalize_question
