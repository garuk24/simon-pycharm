import requests
import random
from basic_word import Basicword

def load_random_word():
    words = [{
    "word": "питон",
     "subwords":  [
         "пони", "тон", "ион", "опт", "пот", "тип", "топ", "пион", "понт"
     ]},
    {
      "word": "набор",
      "subwords":  [
          "бар", "бон", "бор", "раб", "бра", "боа", "нора", "роба", "барон"
     ]},
    {
                        "word": "строка",
                        "subwords": [
         "акр", "акт", "кот", "рак", "орк", "оса", "сок", "ток", "тор", "кора",
         "коса", "сота", "торс", "роса", "скат"
     ]
    }]
    word = random.choice(words)
    return Basicword(word=word['word'], subwords=word['subwords'])



