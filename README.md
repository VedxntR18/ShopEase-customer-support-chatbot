# 🛒 ShopEase Customer Support Chatbot

A modular **NLP-based customer support chatbot** for e-commerce applications, developed in Python as a command-line application.

ShopEase can understand common customer-support queries, classify their intent, extract useful entities such as order IDs and product names, generate contextual responses, and maintain timestamped session logs.

---

## 📌 Overview

Customer-support systems need to interpret natural-language queries and route them to appropriate responses.

This project implements a lightweight NLP-based approach without relying on external APIs or large language models.

The chatbot processes a user's message through the following pipeline:

```text
User Input
    ↓
Text Preprocessing
    ↓
TF-IDF Vectorization
    ↓
Cosine Similarity
    ↓
Intent Classification
    ↓
Entity Extraction
    ↓
Response Personalization
    ↓
Session Logging
```

The system is designed as a modular Python application, with separate components for preprocessing, intent classification, entity extraction, response handling, and logging.

---

## ✨ Features

### 💬 Customer Support

The chatbot can handle common e-commerce support scenarios including:

- Order status and tracking
- Return requests
- Refund status
- Order cancellation
- Product complaints
- Damaged or incorrect products
- Delivery issues
- Payment problems
- Product information
- Discounts and coupons
- Warranty claims
- Human-agent requests

### 🧠 NLP Processing

The project implements several NLP techniques:

- Text normalization
- Lowercase conversion
- Punctuation removal
- Tokenization using NLTK
- Stopword removal
- TF-IDF vectorization
- Cosine similarity-based intent classification

### 🎯 Intent Classification

User queries are converted into TF-IDF vectors and compared against predefined intent patterns using cosine similarity.

The system selects the intent with the highest similarity score.

A confidence threshold is also implemented to prevent low-confidence inputs from being incorrectly classified.

When the similarity score is below the configured threshold, the chatbot uses a fallback response.

### 🔎 Entity Extraction

The chatbot extracts useful entities from user messages using regular expressions and a predefined product catalogue.

Currently supported entities include:

- **Order IDs**
- **Product names**
- **Phone numbers**

Extracted entities can be incorporated into generated responses.

### 🤖 Response Generation

Responses are generated using predefined response templates stored in the intent configuration.

The system can personalize responses using extracted entities such as:

- Order IDs
- Products
- Phone numbers

### 🛡️ Fallback Handling

If the chatbot cannot confidently determine the user's intent, it does not force a potentially incorrect response.

Instead, it returns a fallback message asking the user to:

- Rephrase the query
- Use the `help` command
- Provide a more specific request

### 📝 Session Logging

Each chatbot execution creates a timestamped session log inside the `logs/` directory.

The logs record:

- Session start time
- User messages
- Bot responses
- Conversation flow

The logs are included in the repository as examples of actual chatbot execution and testing.

> **Note:** Do not add real customer information, credentials, private phone numbers, or other sensitive information to committed logs.

---

# 🏗️ Project Architecture

The project is divided into separate modules to keep the application organized and maintainable.

```text
ShopEase-Customer-Support-Chatbot/
│
├── chatbot.py
├── preprocess.py
├── intent_classifier.py
├── ner.py
├── logger.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── data/
│   └── intents.py
│
└── logs/
    ├── chat_log_2026-03-19_12-55-36.txt
    └── chat_log_2026-04-09_12-00-01.txt
```

---

# 📂 Module Description

## `chatbot.py`

Main application/controller.

Responsible for:

- Starting the chatbot
- Displaying the CLI interface
- Accepting user input
- Handling commands
- Calling the intent classifier
- Extracting entities
- Personalizing responses
- Displaying responses
- Recording conversations

---

## `preprocess.py`

Handles NLP preprocessing.

Responsibilities include:

- Lowercase conversion
- Punctuation handling
- Tokenization
- Stopword removal
- Converting processed tokens back into text

---

## `intent_classifier.py`

Implements the intent-classification pipeline.

Uses:

- `TfidfVectorizer`
- Cosine similarity
- Predefined intent patterns
- Confidence threshold
- Fallback responses

The classifier builds its TF-IDF representation from the patterns defined in:

```text
data/intents.py
```

---

## `ner.py`

Handles rule-based entity extraction.

Currently extracts:

- Order IDs
- Product names
- Phone numbers

The implementation uses regular expressions and a predefined product catalogue.

---

## `logger.py`

Handles session logging.

It:

- Creates the `logs/` directory when required
- Generates timestamped log filenames
- Records user messages
- Records chatbot responses
- Stores session timestamps

---

## `data/intents.py`

Contains the chatbot's intent definitions, example patterns, and response templates.

This acts as the knowledge base used by the intent-classification system.

---

# 🧰 Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Core application development |
| NLTK | NLP preprocessing and tokenization |
| Scikit-learn | TF-IDF and cosine-similarity processing |
| TF-IDF | Text feature representation |
| Cosine Similarity | Intent matching |
| Regular Expressions | Entity extraction |
| Colorama | Colored command-line interface |
| File I/O | Session logging |

---

# 📦 Requirements

The project uses the following Python packages:

```text
nltk==3.8.1
scikit-learn==1.4.0
colorama==0.4.6
```

These dependencies are listed in:

```text
requirements.txt
```

---

# 🚀 Installation

## 1. Clone the repository

```bash
git clone https://github.com/VedxntR18/ShopEase-Customer-Support-Chatbot.git
```

Move into the project directory:

```bash
cd ShopEase-Customer-Support-Chatbot
```

---

## 2. Create a virtual environment

### Windows

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv venv
```

Activate it:

```bash
source venv/bin/activate
```

---

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

# 📚 NLTK Resources

The project requires several NLTK resources.

Run:

```bash
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords'); nltk.download('punkt_tab')"
```

This downloads the required tokenizer and stopword resources.

---

# ▶️ Running the Chatbot

Start the application using:

```bash
python chatbot.py
```

You should see a CLI interface similar to:

```text
============================================================
   🛒 Welcome to ShopEase Bot — Customer Support CLI
============================================================
   Ask me about: orders, returns, refunds, products, delivery
   Type 'exit' anytime to quit | Type 'help' for options
============================================================
```

The chatbot will then wait for user input.

---

# 💬 Example Interaction

```text
You: Where is my order ORD-12345?

ShopEase Bot:
Your order information...
```

The system can detect:

```text
Order ID: ORD-12345
```

and use the extracted entity when generating the response.

---

# ⌨️ Commands

| Command | Description |
|---------|-------------|
| `help` | Displays available customer-support topics |
| `exit` | Exits the chatbot |
| `quit` | Exits the chatbot |
| `bye` | Exits the chatbot |
| `goodbye` | Exits the chatbot |
| `q` | Exits the chatbot |

---

# 🧪 Testing & Logs

The repository includes sample session logs generated during chatbot execution.

The logs demonstrate actual interaction flows and can be used to inspect:

- User queries
- Bot responses
- Session timestamps
- Conversation sequences
- Different support scenarios

Example:

```text
[12:00:01] Bot: Hello! I'm your ShopEase customer support assistant.
[12:00:08] You: Where is my order ORD-12345?
[12:00:08] Bot: ...
```

The logs are intentionally retained as part of the project documentation and testing evidence.

---

# 🔐 Privacy & Security Note

This project is intended for educational and demonstration purposes.

The repository should not contain:

- Real customer information
- Passwords
- API keys
- Authentication tokens
- Private credentials
- Sensitive personal information

Before committing new logs, verify that they contain only safe demonstration/test data.

---

# 🧩 Project Design

The application follows a modular structure:

```text
                ┌───────────────────┐
                │    User Input     │
                └─────────┬─────────┘
                          │
                          ▼
                ┌───────────────────┐
                │   Preprocessing   │
                │ NLTK / Tokenizing │
                └─────────┬─────────┘
                          │
                          ▼
                ┌───────────────────┐
                │ Intent Classifier │
                │ TF-IDF + Cosine   │
                │    Similarity     │
                └─────────┬─────────┘
                          │
                          ▼
                ┌───────────────────┐
                │ Entity Extraction │
                │ Regex + Catalogue │
                └─────────┬─────────┘
                          │
                          ▼
                ┌───────────────────┐
                │ Response Handling │
                │ Template + Entity │
                │    Injection      │
                └─────────┬─────────┘
                          │
                          ▼
                ┌───────────────────┐
                │  Session Logger   │
                └───────────────────┘
```

---

# 🎯 Project Objectives

The main objectives of ShopEase are to:

1. Build a lightweight NLP-based customer-support system.
2. Process natural-language customer queries.
3. Classify queries into predefined support intents.
4. Extract useful entities from user messages.
5. Generate contextual responses.
6. Handle unsupported or ambiguous queries through fallback responses.
7. Maintain timestamped chatbot session logs.
8. Demonstrate modular Python application development.

---

# 🔮 Possible Future Improvements

Potential improvements include:

- Web-based user interface
- REST API integration
- Database-backed order lookup
- Real-time order tracking
- Persistent customer sessions
- More advanced NLP models
- Transformer-based intent classification
- Context-aware multi-turn conversations
- Authentication and authorization
- Production-grade logging
- Automated testing
- Deployment as a web service
- Integration with an actual e-commerce backend

---

# 📌 Current Scope

The current version is a **CLI-based educational/demo application**.

It uses predefined intents and responses rather than connecting to a real e-commerce database or production customer-support platform.

No external API or live order-management system is required for the current implementation.

---

# 👨‍💻 Author

## Vedant Vaibhav Rangnekar

B.Tech. Computer Science Engineering  
Artificial Intelligence & Machine Learning

Ramrao Adik Institute of Technology, DY Patil, Navi Mumbai

### Connect

- **GitHub:** https://github.com/VedxntR18
- **Portfolio:** https://vedantrangnekar.in
- **LinkedIn:** https://www.linkedin.com/in/vedant-rangnekar-500944340
- **Email:** vedantrangnekar2005@gmail.com

---

# 📄 License

This project is intended for educational, academic, and portfolio purposes.

Add a formal open-source license here if you decide to distribute the project under one.
