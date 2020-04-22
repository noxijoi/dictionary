from typing import List

import nltk
import pymorphy2
from dataclasses import dataclass
from string import punctuation

from glossary import IMMUTABLES, NOUN, CASES, NUMS, ADJF, NUMR, PRTF, GENDERS, ADJS, PRTS, VERB, PERS

morph = pymorphy2.MorphAnalyzer()

@dataclass(eq=True, order=True, unsafe_hash=True)
class Record:
    pos: str
    base: str
    endings: List[str]


def get_words_from_text(text):
    words = []
    for sentence in nltk.sent_tokenize(text):
        for word in nltk.word_tokenize(sentence):
            if word not in punctuation:
                words.append(word)
    return words


def tag_words(words):
    tagged_words =[]
    for word in words:
        tag = morph.parse(word)
        tagged_words.append(tag)
    return tagged_words

#TODO
def process_word_forms(word_forms):
    pass


def get_record_from_tagged_vord(tagged_word):
    tag = tagged_word[0].tag
    grammemes = tag.grammemes
    pos = tag.POS
    if(pos in IMMUTABLES):
        rec = Record(pos, tag.word, [])
        return rec
    base = ""
    word_forms = []
    if pos == NOUN:
        for num in NUMS:
            for case in CASES.keys():
                word_forms.append(tagged_word.inflect({case,num}))
    elif pos in [ADJF, NUMR, PRTF]:
        for gender in GENDERS.keys():
            for case in CASES.keys():
                word_forms.append(tagged_word.inflect({gender,case}))
        for num in NUMS:
            for case in CASES.keys():
                word_forms.append(tagged_word.inflect({case,num}))
    elif pos in [ADJS, PRTS]:
        for gender in GENDERS.keys():
            word_forms.append(tagged_word.inflect({gender}))
    elif pos == VERB:
        for num in NUMS:
            for per in PERS.keys():
                word_forms.append(tagged_word.inflect({num, per}))
    base, endings = process_word_forms(word_forms)
    rec = Record(pos, base, endings)
    return rec


def create_vocabulary_from_text(text):
    words = get_words_from_text(text)
    tagged_words = tag_words(words)
    records = []
    for tagged_word in tagged_words:
        records.append(get_record_from_tagged_vord(tagged_word))
    return records





