import pymorphy2

morph = pymorphy2.MorphAnalyzer()
tag = morph.parse("читает")
print(tag)