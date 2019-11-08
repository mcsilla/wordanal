from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.tokenize import TweetTokenizer
from nltk.corpus import stopwords



with open('minitext.txt') as f:
   text = f.read()
text = text.replace('’', '\'')
stopWords = set(stopwords.words('english'))

sentences = sent_tokenize(text)

words = TweetTokenizer().tokenize(sentences[1])

wordsFiltered = []

for w in words:
    if w not in stopWords:
        wordsFiltered.append(w)

print(wordsFiltered)

#print data.read(35)

#data = "I am Csilla, the queen. You are my servants... All of you. Do you understand?"

#print(data)

#print(word_tokenize(data))

#print(sent_tokenize(data))
