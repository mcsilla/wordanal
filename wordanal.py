from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.tokenize import TweetTokenizer
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from collections import Counter

with open('J.K.Rowling.-.Harry.Potter.and.the.Philosopher.s.Stone.2012.txt') as f:
    book = f.read()

book = book.replace('’', '\'')
stopWords = set(stopwords.words('english'))

words = [word.lower() for word in TweetTokenizer().tokenize(book)]

filtered_words = [word for word in words if word not in stopWords]

unique_words = set(words)

filtered_unique_words = unique_words - stopWords
        
unique_words_wo_ap = set()
with_ap = []

for w in filtered_unique_words:
    if '\'' in w:
        with_ap.append(w)
    else:
        unique_words_wo_ap.add(w)

ps = PorterStemmer()

stem_dict = {}

PUNCTUATION_INDEX = 31
for word in sorted(unique_words_wo_ap)[PUNCTUATION_INDEX:]:
    stemmed = ps.stem(word)
    if stemmed in stem_dict:
        stem_dict[stemmed].append(word)
    else:
        stem_dict[stemmed] = [word]  

filtered_words_cutted = sorted(filtered_words)[15326:]

frequency_dict = Counter([ps.stem(word) for word in filtered_words_cutted])

def second_item(t):
    return t[1]

print(sorted(frequency_dict.items(), key=second_item, reverse=True))

#print(len(words), len(filtered_words), len(unique_words), len(filtered_unique_words))

