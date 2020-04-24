import time

from vocab import create_vocabulary_from_text, get_words_from_text

test_text = open('test.txt')
text = test_text.read()
words = get_words_from_text(text)
words_count = len(words)
start_time = time.time()
print('start_time ', start_time)
records = create_vocabulary_from_text(text)
end_time = time.time()
print('end_time ', end_time)
print('words in text count: ', words_count)
print('records count: ', len(records))
print('processing time: ', end_time - start_time)

