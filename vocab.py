from typing import List

import pymorphy2
from dataclasses import dataclass

morph = pymorphy2.MorphAnalyzer()

@dataclass(eq=True, order=True, unsafe_hash=True)
class Record:
    pos: str
    base: str
    endings: List[str]

    
def parseNoun(noun):
    pass



