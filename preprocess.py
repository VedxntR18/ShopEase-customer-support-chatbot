import string

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


def _load_stop_words():
    try:
        return set(stopwords.words("english"))
    except LookupError as exc:
        raise RuntimeError(
            "NLTK stopwords are missing. Run 'python setup_nltk.py' before starting the chatbot."
        ) from exc


STOP_WORDS = _load_stop_words()


def to_lowercase(text):
    return text.lower()


def remove_punctuation(text):
    return text.translate(str.maketrans("", "", string.punctuation))


def tokenize(text):
    try:
        return word_tokenize(text)
    except LookupError as exc:
        raise RuntimeError(
            "NLTK tokenizer data is missing. Run 'python setup_nltk.py' before starting the chatbot."
        ) from exc


def remove_stopwords(tokens):
    return [word for word in tokens if word not in STOP_WORDS]


def preprocess(text):
    text = to_lowercase(text)
    text = remove_punctuation(text)
    tokens = tokenize(text)
    return remove_stopwords(tokens)


def tokens_to_string(tokens):
    return " ".join(tokens)
