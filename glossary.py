NOUN = 'NOUN'
ADJF = 'ADJF'
ADJS = 'ADJS'
COMP = 'COMP'
VERB = 'VERB'
INFN = 'INFN'
PRTF = 'PRTF'
PRTS = 'PRTS'
GRND = 'GRND'
NUMR = 'NUMR'
ADVB = 'ADVB'
NPRO = 'NPRO'
PRED = 'PRED'
PREP = 'PREP'
CONJ = 'CONJ'
PRCL = 'PRCL'
INTJ = 'INTJ'

POS = {
    NOUN: 'имя существительное',
    ADJF: 'имя прилагательное',
    ADJS: 'имя прилагательное (краткое)',
    COMP: 'компаратив',
    VERB: 'глагол (личная форма)',
    INFN: 'глагол (инфинитив)',
    PRTF: 'причастие (полное)',
    PRTS: 'причастие (краткое)',
    GRND: 'деепричастие',
    NUMR: 'числительное',
    ADVB: 'наречие',
    NPRO: 'местоимение-существительное',
    PRED: 'предикатив',
    PREP: 'предлог',
    CONJ: 'союз',
    PRCL: 'частица',
    INTJ: 'междометие'
}

IMMUTABLES = [COMP, INFN, ADVB, PRED, PREP, CONJ, PRCL, INTJ]
MUTABLES = [NOUN, ADJS, ADJS, VERB, PRTF, PRTS, GRND, NUMR, NPRO]

CASES_POS = [NOUN, ADJF, PRTF, NUMR, NPRO]
CASES = {
    'nomn': 'именительный',
    'gent': 'родительный',
    'datv': 'дательный',
    'accs': 'винительный',
    'ablt': 'творительный',
    'loct': 'предложный'
}

NUM_POS = [NOUN, ADJF, NUMR, NPRO]
NUMS = {
    'sing': 'единственное',
    'plur': 'множественное'
}

GENDER_POS = [ADJF, ADJS, VERB, NUMR, PRTF, PRTS]
GENDERS = {
    'masc': 'мужской род',
    'femn': 'женский род',
    'neut': 'средний род'
}

PERS_POS =[VERB]

PERS ={
    '1per':'1е лицо',
    '2per':'2е лицо',
    '3per':'3е лицо'
}
