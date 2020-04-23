from typing import List

import nltk
import pymorphy2
from dataclasses import dataclass
from string import punctuation
from difflib import SequenceMatcher

from glossary import IMMUTABLES, NOUN, CASES, NUMS, ADJF, NUMR, PRTF, GENDERS, ADJS, PRTS, VERB, PERS

morph = pymorphy2.MorphAnalyzer()


@dataclass(eq=True, order=True)
class Record:
    pos: str
    base: str
    endings: List[List[str]]
    def __hash__(self):
        return hash(self.base)

def gen_rec_form_str(rec):
    word_forms = generate_word_forms(rec)
    str = ""
    for word_form_block in word_forms:
        for word in word_form_block:
            str += word + ', '
        str += '\n'
    return str

def get_words_from_text(text):
    words = []
    for sentence in nltk.sent_tokenize(text):
        for word in nltk.word_tokenize(sentence):
            if word not in punctuation:
                words.append(word)
    return words


def tag_words(words):
    tagged_words = []
    for word in words:
        tag = morph.parse(word)
        tagged_words.append(tag)
    return tagged_words


def process_word_forms(word_forms):
    endings = []
    wf1 = word_forms[0][0].word
    wf2 = word_forms[0][1].word
    match = SequenceMatcher(None, wf1, wf2) \
        .find_longest_match(0, len(wf1), 0, len(wf2))
    base = wf1[match.a: match.a + match.size]
    for word_form_block in word_forms:
        for i in range(2, len(word_form_block)):
            wf1 = word_form_block[i].word
            match = SequenceMatcher(None, wf1, base).find_longest_match(0, len(wf1), 0, len(base))
            base = wf1[match.a: match.a + match.size]
    for word_form_block in word_forms:
        ending_block = []
        for word in word_form_block:
            word_str = word.word
            ending = word_str[len(base):]
            ending_block.append(ending)
        endings.append(ending_block)
    return base, endings


def get_record_from_tagged_vord(tagged_word):
    parse = tagged_word[0]
    tag = tagged_word[0].tag
    pos = tag.POS
    if pos in IMMUTABLES:
        rec = Record(pos, tag.word, [])
        return rec
    word_forms = []
    if pos == NOUN:
        for num in NUMS:
            word_forms_block = []
            for case in CASES.keys():
                word_forms_block.append(parse.inflect({case, num}))
            word_forms.append(word_forms_block)
    elif pos in [ADJF, NUMR, PRTF]:
        for gender in GENDERS.keys():
            word_forms_block = []
            for case in CASES.keys():
                word_forms_block.append(parse.inflect({gender, case}))
            word_forms.append(word_forms_block)
        for num in NUMS:
            word_forms_block = []
            for case in CASES.keys():
                word_forms_block.append(parse.inflect({case, num}))
            word_forms.append(word_forms_block)
    elif pos in [ADJS, PRTS]:
        word_forms_block = []
        for gender in GENDERS.keys():
            word_forms_block.append(parse.inflect({gender}))
        word_forms.append(word_forms_block)
    elif pos == VERB:
        for num in NUMS:
            word_forms_block = []
            for per in PERS.keys():
                word_forms_block.append(parse.inflect({num, per}))
            word_forms.append(word_forms_block)
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


def generate_word_forms(rec):
    forms = []
    for ending_block in rec.endings:
        word_forms_block = []
        for ending in ending_block:
            form = rec.base + ending
            word_forms_block.append(form)
        forms.append(word_forms_block)
    return forms
