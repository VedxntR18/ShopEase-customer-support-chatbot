import re


PRODUCT_CATALOG = [
    "iphone", "samsung galaxy", "macbook", "dell laptop", "sony headphones",
    "lg tv", "nike shoes", "adidas", "realme", "oneplus", "boat earphones",
    "mi tv", "hp laptop", "lenovo", "asus", "jbl speaker", "canon camera"
]


def extract_order_id(text):
    pattern = r'\bORD-\d{5}\b'
    match = re.search(pattern, text, re.IGNORECASE)
    if match:
        return match.group().upper()
    return None
    

def extract_product_name(text):
    text_lower = text.lower()
    for product in PRODUCT_CATALOG:
        if product in text_lower:
            return product.title()
    return None


def extract_phone_number(text):
    pattern = r'(?:\+91[\s-]?)?[6-9]\d{9}'
    match = re.search(pattern, text)
    if match:
        return match.group()
    return None


def extract_entities(text):
    entities = {
        "order_id": extract_order_id(text),
        "product":  extract_product_name(text),
        "phone":    extract_phone_number(text)
    }
    return entities