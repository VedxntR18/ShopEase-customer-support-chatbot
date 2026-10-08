import random

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from data.intents import INTENTS
from preprocess import preprocess, tokens_to_string


class IntentClassifier:
    CONFIDENCE_THRESHOLD = 0.20

    def __init__(self):
        self.vectorizer = TfidfVectorizer()
        self.patterns = []
        self.tags = []
        self.responses = {}
        self._build_model()

    def _build_model(self):
        for intent in INTENTS:
            tag = intent["tag"]
            self.responses[tag] = intent["responses"]
            for pattern in intent["patterns"]:
                clean = tokens_to_string(preprocess(pattern))
                self.patterns.append(clean)
                self.tags.append(tag)

        self.tfidf_matrix = self.vectorizer.fit_transform(self.patterns)

    def response_for_intent(self, tag):
        return random.choice(self.responses[tag])

    def classify(self, user_input):
        clean_input = tokens_to_string(preprocess(user_input))

        if not clean_input.strip():
            return "unknown", 0.0, self._fallback_response()

        input_vector = self.vectorizer.transform([clean_input])
        similarities = cosine_similarity(input_vector, self.tfidf_matrix).flatten()

        best_index = similarities.argmax()
        best_score = similarities[best_index]
        best_tag = self.tags[best_index]

        if best_score < self.CONFIDENCE_THRESHOLD:
            return "unknown", round(best_score, 2), self._fallback_response()

        return best_tag, round(best_score, 2), self.response_for_intent(best_tag)

    def _fallback_response(self):
        fallbacks = [
            "I'm sorry, I didn't understand that. Could you rephrase?\n"
            "  💡 Try: 'track my order', 'return item', 'refund status'",
            "Hmm, I'm not sure about that.\n"
            "  💡 Type 'help' to see all topics I can assist with!",
            "I couldn't catch that. Could you be more specific?\n"
            "  💡 Example: 'Where is my order ORD-12345?'",
        ]
        return random.choice(fallbacks)
