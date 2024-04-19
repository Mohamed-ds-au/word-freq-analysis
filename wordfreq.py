from nltk.corpus import stopwords
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.probability import FreqDist
nltk.download('punkt')
nltk.download("stopwords")

stop_word = stopwords.words("english")

with open("paragraphs.txt", 'r') as file:
    text = file.read()

words = word_tokenize(text)
words_without_stop = []

for word in words:
    if word.lower() not in stop_word:
        words_without_stop.append(word)

fq = FreqDist(word.lower() for word in words_without_stop)
print(fq.items())
