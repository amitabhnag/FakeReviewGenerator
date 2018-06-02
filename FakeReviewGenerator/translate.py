"""
This module translates text passed to it as a parameter, into Chinese and back to English.
This is a post processing step to smoothen the output.

Prerequisites:
    pip install googletrans

Functions:
    translate()

Author: Gautam Moogimane.
"""

from googletrans import Translator

def translate(word):
    """Translate any word/phrases from English to Chinese, the back to English.

    Args:
        word: input string.

    Output:
        english translations.
    """
    translator = Translator()
    chin_text = translator.translate(word, src='en', dest='zh-cn')
    #print(chin_text.text)
    eng_text = translator.translate(chin_text.text, src='zh-cn', dest='en')
    #print(eng_text.text)
    return eng_text.text
    