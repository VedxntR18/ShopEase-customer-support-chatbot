# 🛒 ShopEase Customer Support Chatbot

A modular **NLP-based customer-support chatbot** for e-commerce applications, built in Python as a command-line application.

ShopEase demonstrates a classic intent-classification workflow using **NLTK preprocessing, TF-IDF, cosine similarity, rule-based entity extraction, response templates, fallback handling, and session logging**.

> **Scope:** This is an educational/demo NLP application. It does **not** connect to a real order database, payment gateway, customer account system, or live support platform.

## Architecture

```text
User Input
    ↓
NLTK Preprocessing
    ↓
TF-IDF Vectorization
    ↓
Cosine Similarity
    ↓
Intent Classification
    ↓
Rule-based Entity Extraction
    ↓
Response Personalization
    ↓
Session Logging
```

## Features

- Order-status and tracking intent
- Returns and refunds
- Order cancellation
- Product complaints
- Delivery and payment issues
- Product information
- Discounts and coupons
- Warranty questions
- Human-agent request intent
- Frustration/fallback handling
- Order ID, product, and Indian phone-number extraction
- Timestamped session logs
- Confidence threshold for unknown queries
- Entity-aware handling for standalone order IDs

## NLP Approach

### Preprocessing

The input is:

1. converted to lowercase
2. stripped of punctuation
3. tokenized with NLTK
4. filtered using NLTK English stopwords

### Intent Classification

The classifier:

1. builds a TF-IDF representation from the patterns in `data/intents.py`
2. transforms each user message into the same feature space
3. computes cosine similarity against all intent patterns
4. selects the highest-scoring intent
5. falls back to an unknown response when the score is below `0.20`

Responses are selected from predefined templates for the predicted intent.

### Entity Extraction

`ner.py` uses regular expressions and a small product catalogue to extract:

- Order IDs such as `ORD-12345`
- Indian phone numbers
- Product names such as `Sony Headphones`

Entity extraction is separate from intent classification so the two components can be tested independently.

## Project Structure

```text
ShopEase-customer-support-chatbot/
├── chatbot.py
├── preprocess.py
├── intent_classifier.py
├── ner.py
├── logger.py
├── setup_nltk.py
├── data/
│   └── intents.py
├── tests/
│   ├── test_ner.py
│   └── test_logger.py
├── logs/
│   └── sample session logs
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation

### 1. Clone

```bash
git clone https://github.com/VedxntR18/ShopEase-customer-support-chatbot.git
cd ShopEase-customer-support-chatbot
```

### 2. Create a virtual environment

Windows:

```cmd
python -m venv venv
venv\Scripts\activate
```

Linux/macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Download NLTK resources

```bash
python setup_nltk.py
```

This downloads the tokenizer and stopword resources required by the application.

## Run

```bash
python chatbot.py
```

The chatbot provides a CLI with commands such as:

| Command | Purpose |
|---|---|
| `help` | Show supported customer-support topics |
| `exit` | End the session |
| `quit` | End the session |
| `bye` | End the session |
| `goodbye` | End the session |
| `q` | End the session |

Debug classification output is disabled by default. Set `SHOW_DEBUG = True` in `chatbot.py` when inspecting intent scores and extracted entities during development.

## Example

```text
You: Where is my order ORD-12345?

ShopEase Bot:
Please share your Order ID (format: ORD-XXXXX) and I'll look it up for you.
(Order detected: ORD-12345)
```

For a standalone order ID:

```text
You: ORD-12345

ShopEase Bot:
Demo order status for ORD-12345: the simulated order is currently
OUT FOR DELIVERY and is expected by tomorrow.
```

These statuses are **simulated template responses**, not live order lookups.

## Testing

Run:

```bash
pytest tests/ -v
```

The current automated tests cover:

- Order ID extraction
- Product extraction
- Phone-number extraction
- Log-file creation and message persistence

The repository also contains historical/sample chatbot session logs. These are retained as testing evidence and should contain demonstration data only.

## Logging

Every new session creates a timestamped file under `logs/`.

The logger resolves the log directory relative to the project file, so running the chatbot from another working directory does not redirect logs into an unexpected location.

Do not commit real customer information, credentials, private phone numbers, or other sensitive information.

## Current Scope and Limitations

This project is an **academic/demo NLP application**, not a production customer-support platform.

- Intent classification uses TF-IDF + cosine similarity rather than a transformer model.
- Intents and responses are predefined in `data/intents.py`.
- Entity extraction is rule-based and catalogue-limited.
- There is no real order-management database.
- Order status, refunds, coupons, delivery outcomes, and agent handoffs are simulated response templates.
- There is no authentication or customer-account integration.
- The current interface is CLI-only.
- The sample logs document earlier experiments and may contain classification failures; they are evidence of the development process rather than a formal accuracy benchmark.

## Future Improvements

- Web UI or REST API
- Database-backed order lookup
- Real order tracking integration
- Context-aware multi-turn conversations
- Larger intent dataset
- Automated intent-classification accuracy benchmark
- Transformer-based intent model
- Authentication and authorization
- Production logging and monitoring
- Deployment as a web service

## Author

**Vedant Vaibhav Rangnekar**  
B.Tech. Computer Science Engineering — Artificial Intelligence & Machine Learning  
Ramrao Adik Institute of Technology, DY Patil, Navi Mumbai

- GitHub: https://github.com/VedxntR18
- Portfolio: https://vedantrangnekar.in
- LinkedIn: https://www.linkedin.com/in/vedant-rangnekar-500944340

## License

This project is intended for educational, academic, and portfolio purposes. Add a formal open-source license if you decide to distribute it under one.
