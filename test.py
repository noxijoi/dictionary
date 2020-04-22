import pymorphy2

morph = pymorphy2.MorphAnalyzer()
print(morph.parse("читает"))