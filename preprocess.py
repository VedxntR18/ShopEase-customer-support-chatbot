import re
import string
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

STOP_WORDS = set(stopwords.words('english'))

def to_lowercase(text):
    return text.lower()

def remove_punctuation(text):
    return text.translate(str.maketrans('', '', string.punctuation))

def tokenize(text):
    return word_tokenize(text)

def remove_stopwords(tokens):
    return [word for word in tokens if word not in STOP_WORDS]

def preprocess(text):
    text = to_lowercase(text)
    text = remove_punctuation(text)
    tokens = tokenize(text)
    tokens = remove_stopwords(tokens)
    return tokens

def tokens_to_string(tokens):
    return " ".join(tokens)