"""
    Test the module /gdpy/parsers.py
"""
from gdpy.gdpy_app.parsers import convert_specials_characters, \
    remove_forbid_words


def test_convert_specials_characters():
    question = "Bonjour ʦ, est-ce que ʯ cônnais le \
chemin de la Liberté φ Boston sud Ѯ ?"
    normal_question = convert_specials_characters(question)
    assert normal_question == "Bonjour , est-ce que  connais \
le chemin de la Liberte  Boston sud  ?"


def test_XSS_flaw():
    question = "<script>location.href=\
'http://www.your_friend.org/upgrade.php?'</script>"
    normal_question = remove_forbid_words(question)
    assert '<' not in normal_question


def test_remove_forbid_words():
    question = "Bonjour GrandPy, est-ce que tu connais \
le chemin de la Liberte de Boston:sud ?"
    question_without_forbid_words = remove_forbid_words(question)
    assert question_without_forbid_words == "chemin liberte boston sud"
