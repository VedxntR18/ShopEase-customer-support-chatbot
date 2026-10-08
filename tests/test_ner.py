from ner import extract_entities


def test_order_id_extraction():
    entities = extract_entities("Please track order ord-48291")
    assert entities["order_id"] == "ORD-48291"


def test_product_extraction():
    entities = extract_entities("My Sony Headphones are damaged")
    assert entities["product"] == "Sony Headphones"


def test_phone_extraction():
    entities = extract_entities("Call me on +91 9876543210")
    assert entities["phone"] == "+91 9876543210"


def test_no_entities():
    entities = extract_entities("I need help with something")
    assert entities == {"order_id": None, "product": None, "phone": None}
