from gdpy.gdpy_app.words import STOP_WORDS, SKIP_WORDS
import re
import unicodedata

"""
Two methods to clean the user's question
"""


def normalize(question: str) -> str:
    """
        Convert specials characters in ``question``
        and remove banned words.
        See also ``convert_specials_characters``
        and ``remove_forbid_words`` methods
    """
    question = convert_specials_characters(question)
    return remove_forbid_words(question)


def convert_specials_characters(question: str) -> str:
    """
        Encode all characters ``question`` in ASCII characters
    """
    question = unicodedata.normalize('NFKD', question)
    return question.encode('ASCII', 'ignore').decode('utf-8')


def remove_forbid_words(question: str) -> str:
    """`
        Remove all stop word in ``question``
    """
    fordib_words = STOP_WORDS.union(SKIP_WORDS)

    normalize_question = ' '.join(
        (word
            for word in re.split('[^a-zA-Z0-9_]+', question.lower())
            if word and word not in fordib_words))

    return normalize_question
