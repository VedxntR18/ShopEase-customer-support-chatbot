import pytest

from intent_classifier import IntentClassifier


@pytest.fixture(scope="module")
def classifier():
    return IntentClassifier()


def test_order_status_intent(classifier):
    tag, confidence, _ = classifier.classify("Where is my order?")
    assert tag == "order_status"
    assert confidence >= 0.20


def test_frustration_intent(classifier):
    tag, confidence, _ = classifier.classify("I hate this site")
    assert tag == "frustration"
    assert confidence >= 0.20


def test_unknown_intent(classifier):
    tag, confidence, _ = classifier.classify("quantum spaceship banana")
    assert tag == "unknown"
    assert confidence < 0.20
